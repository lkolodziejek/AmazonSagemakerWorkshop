# Amazon Sagemaker Workshop

#### Welcome to Amazon Sagemaker Workshops. Going through this material you will learn how to use [_Amazon SageMaker_](https://aws.amazon.com/sagemaker/) to build, train, retraining and deploy a machine learning (ML) model in AWS. We will use Amazon SageMaker Studio - the first fully integrated development environment for machine learning through all exercise. This workshop is divided into 3 following labs:

* [**_Lab 1_**](www.google.com) - Feature Engineering, Training (using built in algorithm - XGBoost), Deployment, Inferention
* [**_Lab 2_**](www.google.com) - Feature Engineering, Training (using your own scikit-learn scripts), Deployment, Inferention
* [**_Lab 3_**](www.google.com) - Auto ML on Amazon Sagemaker

# Prerequisite
Create an S3 bucket in the same region as your Amazon SageMaker studio. Follow the link for detailed steps if required (https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html). This bucket is used to store intermediate results computed during SageMaker studio.

# Launch Amazon SageMaker Studio
Amazon SageMaker Studio is a web-based, integrated development environment (IDE) for machine learning that lets you build, train, debug, deploy, and monitor your machine learning models. Studio provides all the tools you need to take your models from experimentation to production while boosting your productivity.

Here are the one-time steps for onboarding to Amazon SageMaker Studio using Quick Start:
1. Open AWS console and switch to “_eu-west-2_” (Ireland) region. (You can choose other region as well wherever [_SageMaker Studio is available_](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html))
2. Under services search for “_Amazon SageMaker_”
3. Click on “_Amazon SageMaker Studio_”
4. Click on “_Quick start_”
5. Define “_User name_” as “_machinelearning_”
6. Select “_Create a new role_” under Execution role. Also make sure you are selecting specific S3 Bucket where all dataset and ML models will be pushed. If you don’t have any pre created S3 Bucket created then please create the same in “_us-east-2_” region.
7. Enter the Role ARN in “_Custom IAM role ARN_” created on step 6 (not required when creating new role)
8. Click “_Submit_”

![](https://sagemaker-immersionday.workshop.aws/lab1/media/image3.png)

9. Once Amazon SageMaker Studio is ready then click on “Open Studio”
10. You will be redirected to a new web tab that looks something like below:

![](https://sagemaker-immersionday.workshop.aws/lab1/media/image4.png)
