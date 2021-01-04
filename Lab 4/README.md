# Lab 4 - Model retraining

In this lab, you will get hands-on with model retraining. We will build simple but fully automated solution to retrain the model whenever a new dataset is delivered. To make our live simpler we will use the best candidate we have selected in Lab 3. Our pipline works as follows:

- You 


Losing customers is costly for any business. Identifying unhappy customers early on gives you a chance to offer them incentives to stay. This lab describes using machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. We will use the same data set as we did in **_Lab 1_** as we are already familiar with it.


In this lab SageMaker Autopilot first inspects your data set, and runs a number of model candidates to figure out the optimal combination of data preprocessing steps, machine learning algorithms and hyperparameters. It then uses this combination to train an Inference Pipeline, which you can easily deploy either on a real-time endpoint, or use it for batch processing.  
  
  
- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setup)
- [_Data_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#data)
- [_Setting up the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setting-up-the-amazon-sagemaker-autopilot-job)
- [_Launching the Amazon Sagemaker Autopilot Job_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#launching-the-amazon-sagemaker-autopilot-job)


**Ok, lest start the lab!!**

# Setup

1. We will start with opening Notebook `autopilot_customer_churn.ipynb` in “AmazonSagemakerWorkshop/Lab 3” folder. We will skip detailed instruction how to procees as you are the expert now.  
  
  **Zdjęcie tutaj, jak wygląda katalog Lab 3!**
