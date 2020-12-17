# Lab 1

**Feature Engineering, Training (using built in algorithm - XGBoost), Deployment, Inferention**

In this lab, you will learn how to use Amazon SageMaker to build, train, and deploy a machine learning (ML) model. We will use the popular XGBoost ML algorithm for this exercise. Amazon SageMaker is a modular, fully managed machine learning service that enables developers and data scientists to build, train, and deploy ML models at scale.

Taking ML models from concept to production is typically complex and time-consuming. You have to manage large amounts of data to train the model, choose the best algorithm for training it, manage the compute capacity while training it, and then deploy the model into a production environment. Amazon SageMaker reduces this complexity by making it much easier to build and deploy ML models. After you choose the right algorithms and frameworks from the wide range of choices available, Amazon SageMaker manages all of the underlying infrastructure to train your model at petabyte scale, and deploy it to production.

In this lab, you will assume the role of a machine learning developer. Your task is to identify unhappy customers early on to have a chance to offer them incentives to stay. Losing customers is costly for any business. You will use notebook `xgboost_customer_churn.ipynb` that describes how to use machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. ML models rarely give perfect predictions though, so this notebook is also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.

# Data Preparation

In this step you will use your Amazon SageMaker Studio notebook to preprocess the data that you need to train your machine learning model.

1. File → New Terminal
2. Then clone the git repo using below command:

`git clone https://github.com/pawelmoniewski/AmazonSagemakerWorkshop.git`

3. After completion of step 2 you will have “_AmazonSagemakerWorkshop_” folder created in “_left panel_” of the studio:

![](https://user-images.githubusercontent.com/36265995/102468789-468be000-4052-11eb-9c06-039df000d2c7.png)

4. In the left side panel choose “_AmazonSagemakerWorkshop_”, than “_Lab 1_” and open xgboost_customer_churn.ipynb
#### WSTAW TU ZDJECIE
5. Select the kernel for your notebook: “_Python 3(Data Science)_”

![](https://user-images.githubusercontent.com/36265995/102474260-b7ce9180-4058-11eb-8b0d-3c6c068803e7.png)

6. In the next cell you will load the dataset into a pandas dataframe


![](https://user-images.githubusercontent.com/36265995/102479357-15fe7300-405f-11eb-9bc7-a74d48473499.png)



5. In the given notebook replace the bucket name with the name of the bucket that you would like to use for this tutorial as shown below:

![](https://user-images.githubusercontent.com/36265995/102475949-ce75e800-405a-11eb-935e-636c0be8cf3d.png)

6. Execute the first two cells by pressing `Shift`+`Enter` in each of the cells. While the code runs, an `*` appears between the square brackets. After a few seconds, the code execution will complete, the `*` will be replaced with the number `1`.

This code will import some libraries in your Jupyter notebook environment:

![](https://user-images.githubusercontent.com/36265995/102478214-a20f9b00-405d-11eb-9e6c-6cb03d45c0d6.png)

Now, Let’s download the dataset by running the next cell.

![](https://user-images.githubusercontent.com/36265995/102478876-6d501380-405e-11eb-80d3-ab230da23d00.png)
