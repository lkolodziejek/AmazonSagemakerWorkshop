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

In the line 8 `ENDPOINT_NAME` environment variable was defined. This is the name of the Amazon Sagemaker endpoint that we created while deploying the model. To get this endpooint name please go back to section [_Deploy the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#deploy-the-model) where you can find it. In this case the neme is: `sagemaker-xgboost-2020-12-17-14-26-01-562`.
