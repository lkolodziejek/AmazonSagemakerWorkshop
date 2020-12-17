# Lab 1

**Feature Engineering, Training (using built in algorithm - XGBoost), Deployment, Inferention**

In this lab, you will learn how to use Amazon SageMaker to build, train, and deploy a machine learning (ML) model. We will use the popular XGBoost ML algorithm for this exercise. Amazon SageMaker is a modular, fully managed machine learning service that enables developers and data scientists to build, train, and deploy ML models at scale.

Taking ML models from concept to production is typically complex and time-consuming. You have to manage large amounts of data to train the model, choose the best algorithm for training it, manage the compute capacity while training it, and then deploy the model into a production environment. Amazon SageMaker reduces this complexity by making it much easier to build and deploy ML models. After you choose the right algorithms and frameworks from the wide range of choices available, Amazon SageMaker manages all of the underlying infrastructure to train your model at petabyte scale, and deploy it to production.

In this lab, you will assume the role of a machine learning developer. Your task is to identify unhappy customers early on to have a chance to offer them incentives to stay. Losing customers is costly for any business. You will use notebook `xgboost_customer_churn.ipynb` that describes how to use machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. ML models rarely give perfect predictions though, so this notebook is also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.

# Data Preparation

In this step you will use your Amazon SageMaker Studio notebook to preprocess the data that you need to train your machine learning model.

1. File → New Terminal
2. Then clone the git repo using below command:

`git clone https://github.com/aws-samples/amazon-sagemaker-immersion-day.git`

3. After completion of step 2 you will have “_XXXXXXXXXXX_” folder created in “_left panel_” of the studio:
#### WSTAW TU ZDJECIE
4. In the left side panel choose XXXXXXXXXXXXX and open xgboost_customer_churn.ipynb
#### WSTAW TU ZDJECIE


