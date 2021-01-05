# Lab 4 - Model retraining

In this lab, you will get hands-on with model retraining. We will build simple but fully automated solution to retrain the model whenever a completely new dataset is delivered. To make our live simpler we will use the best candidate we have selected in Lab 3. Our pipeline works as follows:

1. You collect a new data and add it on top existing training dataset;
2. With this new training dataset you retrain the model that was selected as a best candidate in Lab 3;
3. We will use the same algorithm, input and output configuration, resource configuration, stopping condition and hyper parameters configuration as well;
4. With this configuration you will start the training job and build the model;
5. Finally you will update endpoint from Lab 3 with the new model;  
  
    
- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setup)
- [_Data_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#data)
- [_Setting up the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setting-up-the-amazon-sagemaker-autopilot-job)
- [_Launching the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#launching-the-amazon-sagemaker-autopilot-job)


**Ok, lest start the lab !!!**

# Setup

1. We will start by creating a new role that we will use to execute our lambda function. To do this, login to AWS console and navigate to IAM sevice. Then select _"Role"_ in left menu. Select _"Create role"_ button:  
  
![CreateRole](https://user-images.githubusercontent.com/36265995/103633666-56f2f480-4f46-11eb-9cf0-923230b20e67.png)
    
  
2. Pick _"Lamda"_ service in “Choose a use case” section. Next, select “Next: Permissions” button.  
  
  ![](https://user-images.githubusercontent.com/36265995/102612322-cee0b280-4130-11eb-9557-b58c668c86d6.png)
  
