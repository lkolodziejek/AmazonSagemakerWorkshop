# Lab 4 - Model retraining

In this lab, you will get hands-on with model retraining. We will build simple but fully automated solution to retrain the model whenever a completely new dataset is delivered. To make our live simpler we will use the best candidate we have selected in Lab 3. Our pipeline works as follows:

- [x] You collect a new data and add it on top existing training dataset;
- [x] With this new training dataset you retrain the model that was selected as a best candidate in Lab 3;
- [x] We will use the same algorithm, input and output configuration, resource configuration, stopping condition and hyper parameters configuration as well;
- [x] With this configuration you will start the training job and build the model;
- [x] Finally you will update endpoint from Lab 3 with the new model;  
  
**In this lab we will go through the following sections:**

- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%204/README.md#setup)
- [_Lambda function for retraining process_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%204/README.md#lambda-function-for-retraining-process)
- [_Setting up the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setting-up-the-amazon-sagemaker-autopilot-job)
- [_Launching the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#launching-the-amazon-sagemaker-autopilot-job)


**Ok, lest start the lab !!!**

# Setup

1. We will start by creating a new role that we will use to execute our lambda function. To do this, login to AWS console and navigate to IAM sevice. Then select _"Role"_ in left menu. Select _"Create role"_ button:  
  
![CreateRole](https://user-images.githubusercontent.com/36265995/103634459-60c92780-4f47-11eb-8e03-218bedaf60b1.png)
    
  
2. Pick _"Lamda"_ service in “Choose a use case” section. Next, select “Next: Permissions” button.  
  
  ![](https://user-images.githubusercontent.com/36265995/102612322-cee0b280-4130-11eb-9557-b58c668c86d6.png)
  
  
3. In search box tap `AmazonSageMakerFullAccess` and check this permissions policy. Then press _"Next: Tags"_ button:
  
  
![Next-Tags](https://user-images.githubusercontent.com/36265995/103635487-ded9fe00-4f48-11eb-9f22-563091066228.png)  
  
  
4.  Select “Next: Review” and provide name for the role. Then press _"Ceate role"_:
  
  
  ![CreateRoleFinal](https://user-images.githubusercontent.com/36265995/103635875-73446080-4f49-11eb-8ee8-f555f755fa03.png)
  
5. We have successfully completed this part of lab. Now move on to the next section.


# Lambda function for retraining process

In this section we will build lambda function that orchestrates model retraining process. Please keep in mind that AWS Lambda service is limited to 15 minutes of execution period only. In our case it is more then we need. Still if you need longer execution period you should consider AWS Step Function instead.

1. Navigate to AWS Lambda service dashboard and pick _"Create function"_ button.  
  
  
![Create Function](https://user-images.githubusercontent.com/36265995/103642448-704e6d80-4f53-11eb-8bc6-b0e89de0cbd6.png)
  
  
2. Provide a name for your lambda functiony and select **_Python 3.7_** as runtime. Next, expand “_Change default execution role_” in “_Permissions_” section. Select “_Use an existing role_” and select the role you created few steps earlier. Finally select “_Create function_”

![](https://user-images.githubusercontent.com/36265995/102625458-d199d280-4145-11eb-96a4-638fb7756a18.png)
  
  
3. Now identify values for environment variables that we will use in lambda function:

- ___PREFIX___: We will use this character string to prefix all artifacts that we will produce during retraining process. This will make your navigation through console much easier. I will use: `MyRetrainerPrefix_`;
- ___AUTO_ML_JOB_NAME___: The value of `AutoMLJobName` parameter was returned when we launched Amazon Sagemaker Auto Pilot jos in lab 3. In my case it is: `automl-churn-22-13-32-04`. Plese refer to [_Launching the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#launching-the-amazon-sagemaker-autopilot-job) to find your value.
- ___ENDPOINT_NAME___: The name of the endpoint where we deployed our model in lab 3. In my case it is: `tuning-job-1-68b0d889fb234badb4-012-ef007be004-11-32-13-ep`. Plese refer to [_Deploy the best model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#deploy-the-best-model) to find your value.
  
Now please set up all above environment variables for lambda function. You should see something like that in the dashboard:

![EviorementVariables](https://user-images.githubusercontent.com/36265995/103646687-5a907680-4f5a-11eb-90fb-056630939c29.png)

4. Increase the execution timeout to 15 minutes for your lambda function.

5. Now, copy the content of the `autopilot-customerchurn-retrainer-lambda.py` file into lambda code editor.

Ok. Now we can dig into details of this code:  
- In lines 1-7 we do very basic things. Basically we import necessary libraries and initialize boto client for Amazon Sagemaker service.
- In line 8 we start defining lambda function. This is the entry point for handling the event that will be generated/triggered when we put new dataset in S3 bucket. We will get to that shortly.
- In lines 9-14 we initialize variables according to the environment variables configuration.
- In lines 15-16 we define timestamp suffix for better traceability of output artifact during retraining process.
- In lines 18-20 finally we get a handler to the best canidate that was selecterd in the lab 3. With this handler we can reach all information that we ned to run training job again.
- In line 24 we do a very tricky thing. As we have already trained the best candidate earlier we have also received all metric definitions. We don't want to pass this information to training job a priori so we delete this entry. If you skip this part you will get an error.
- In line 27 we define name for new training job.
- In lines 29-39 we start the training job.
- In line 42 we wait until the training job is done to proceed with next steps.
- In line 45 we define name for the new model.
- In line 46 we create model using best_candidate['InferenceContainers'] entry to define things like url to store model.
- Finally in lines 49-53 we create endpoint configuration and update endpoint created in lab 3 with the newly trained model.

6. Now let's trigger AWS lambda function whenever new training dataset will appear in S3 bucket. Press _"+ Add trigger"_ in the lambda Designer:
  
  ![AddTrigger](https://user-images.githubusercontent.com/36265995/103658529-9c75e880-4f6b-11eb-8c67-954ea9effebd.png)
  
  
7. Ok. Now configure the trigger as below. Press _"Add"_ when you done.
  
  ![AddTriggerConf](https://user-images.githubusercontent.com/36265995/103659957-53269880-4f6d-11eb-82f4-36aaff5ec92c.png)
  
  
 ___Congratulations !!___! You have successfully completed this section. 
 
 # Testing
 
 Finally we can test our retraining process. Please follow below steps.
 
 1. In your S3 bucket that you have created in lab 3 navigate to folder: `csagemaker/autopilot-churn/train/`;
 
 ![S3](https://user-images.githubusercontent.com/36265995/103660854-5e2df880-4f6e-11eb-81ce-5201703194b8.png)
 
 2. Download the file `train_data.csv`. Then delete this file from your bucket and upload once again. This will trigger lambda function.
 
 We didn't modify the `train_data.csv` file as it was not our goal here. We upload the same file triggering the lambda function.
 
 3. Verify if new training job has launched
