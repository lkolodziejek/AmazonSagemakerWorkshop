import json
import boto3
import os
import datetime

sm = boto3.client('sagemaker')

def lambda_handler(event, context):

    # Get environment variables 
    prefix = os.environ['PREFIX']
    automl_job_name = os.environ['AUTO_ML_JOB_NAME']
    endpoint_name = os.environ['ENDPOINT_NAME']
    
    # Helper variable with suffix for output artifacts naming
    timestamp_suffix = str(datetime.datetime.today()).replace(' ', '-').replace(':', '-').rsplit('.')[0]

    # 
    best_candidate = sm.describe_auto_ml_job(AutoMLJobName=automl_job_name)['BestCandidate']
    job_name = best_candidate["CandidateName"];
    job = sm.describe_training_job(TrainingJobName=job_name)
    
    # When calling the CreateTrainingJob operation: You can't override the metric definitions for Amazon SageMaker algorithms.
    job['AlgorithmSpecification'].pop('MetricDefinitions',None)
    
    #Creating new training job.
    new_job_name = prefix + timestamp_suffix + "-job";
    
    sm.create_training_job(
        TrainingJobName=new_job_name,
        AlgorithmSpecification=job['AlgorithmSpecification'],
        RoleArn=job['RoleArn'],
        InputDataConfig=job['InputDataConfig'],
        OutputDataConfig=job['OutputDataConfig'],
        ResourceConfig=job['ResourceConfig'],
        StoppingCondition=job['StoppingCondition'],
        HyperParameters=job['HyperParameters'] if 'HyperParameters' in job else {},
        Tags=job['Tags'] if 'Tags' in job else []
    )

    #Waiting for job to finish training
    sm.get_waiter('training_job_completed_or_stopped').wait(TrainingJobName = new_job_name);

    #Creating Model
    model_name = prefix + timestamp_suffix + "-model";
    model_arn = sm.create_model(Containers=best_candidate['InferenceContainers'], ModelName=model_name, ExecutionRoleArn=job['RoleArn'])

    #Creating Endpoint Configuration
    epc_name = prefix + timestamp_suffix + "-epc"
    ep_config = sm.create_endpoint_config(EndpointConfigName = epc_name, ProductionVariants=[{'InstanceType': 'ml.m4.xlarge', 'InitialInstanceCount': 1, 'ModelName': model_name,'VariantName': 'main'}])

    #Updatin Endpoint
    sm.update_endpoint( EndpointName=endpoint_name, EndpointConfigName=epc_name)

    return "Ok";
