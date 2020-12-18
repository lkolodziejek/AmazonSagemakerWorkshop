# Lab 1

**Feature Engineering, Training (using built in algorithm - XGBoost), Deployment, Inferention**

In this lab, you will learn how to use Amazon SageMaker to build, train, and deploy a machine learning (ML) model. We will use the popular XGBoost ML algorithm for this exercise. Amazon SageMaker is a modular, fully managed machine learning service that enables developers and data scientists to build, train, and deploy ML models at scale.

Taking ML models from concept to production is typically complex and time-consuming. You have to manage large amounts of data to train the model, choose the best algorithm for training it, manage the compute capacity while training it, and then deploy the model into a production environment. Amazon SageMaker reduces this complexity by making it much easier to build and deploy ML models. After you choose the right algorithms and frameworks from the wide range of choices available, Amazon SageMaker manages all of the underlying infrastructure to train your model at petabyte scale, and deploy it to production.

In this lab, you will assume the role of a machine learning developer. Your task is to identify unhappy customers early on to have a chance to offer them incentives to stay. Losing customers is costly for any business. You will use notebook `xgboost_customer_churn.ipynb` that describes how to use machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. ML models rarely give perfect predictions though, so this notebook is also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.


- [_Data Preparation_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#data-preparation)
- [_Train & Tune the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#train--tune-the-model)
- [_Deploy the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#deploy-the-model)


# Data Preparation

In this step you will use your Amazon SageMaker Studio notebook to preprocess the data that you need to train your machine learning model.

1. File → New Terminal

2. Then clone the git repo using below command:
  
`git clone https://github.com/pawelmoniewski/AmazonSagemakerWorkshop.git`
  
3. After completion of step 2 you will have “_AmazonSagemakerWorkshop_” folder created in “_left panel_” of the studio:
  
  
  
![](https://user-images.githubusercontent.com/36265995/102468789-468be000-4052-11eb-9c06-039df000d2c7.png)
  
  
  
4. In the left side panel choose “_AmazonSagemakerWorkshop_”, than “_Lab 1_” and open xgboost_customer_churn.ipynb


 WSTAW TU ZDJECIE


5. Select the kernel for your notebook: “_Python 3(Data Science)_”



![](https://user-images.githubusercontent.com/36265995/102474260-b7ce9180-4058-11eb-8b0d-3c6c068803e7.png)




6. In the given notebook replace the bucket name with the name of the bucket that you would like to use for this tutorial as shown below:



![](https://user-images.githubusercontent.com/36265995/102475949-ce75e800-405a-11eb-935e-636c0be8cf3d.png)



7. Execute the first two cells by pressing `Shift`+`Enter` in each of the cells. While the code runs, an `*` appears between the square brackets. After a few seconds, the code execution will complete, the `*` will be replaced with the number `1`.



This code will import some libraries in your Jupyter notebook environment:



![](https://user-images.githubusercontent.com/36265995/102478214-a20f9b00-405d-11eb-9e6c-6cb03d45c0d6.png)



Now, Let’s download the dataset by running the next cell.



![](https://user-images.githubusercontent.com/36265995/102478876-6d501380-405e-11eb-80d3-ab230da23d00.png)



8. In the next cell you will load the dataset into a pandas dataframe



![](https://user-images.githubusercontent.com/36265995/102479357-15fe7300-405f-11eb-9bc7-a74d48473499.png)



9. Now let’s explore the data and understand the data distribution for each feature:



![](https://user-images.githubusercontent.com/36265995/102480320-64f8d800-4060-11eb-86f1-230b873bc6b3.png)



![](https://user-images.githubusercontent.com/36265995/102480376-78a43e80-4060-11eb-8377-f5477668cca9.png)



11. `Phone` takes on too many unique values to be of any practical use. It's possible parsing out the prefix could have some value, but without more context on how these are allocated, we should avoid using it. Most of the numeric features are surprisingly nicely distributed, with many showing bell-like gaussianity.  `VMail Message` being a notable exception (and `Area Code` showing up as a feature we should convert to non-numeric).



![](https://user-images.githubusercontent.com/36265995/102481237-bbb2e180-4061-11eb-8ff5-0ae68ca680d1.png)



12. Next let's look at the relationship between each of the features and our target variable.



![](https://user-images.githubusercontent.com/36265995/102482986-5f04f600-4064-11eb-9a2d-67f66af58243.png)



Interestingly we see that churners appear:
- Fairly evenly distributed geographically
- More likely to have an international plan
- Less likely to have a voicemail plan
- To exhibit some bimodality in daily minutes (either higher or lower than the average for non-churners)
- To have a larger number of customer service calls (which makes sense as we'd expect customers who experience lots of problems may be more likely to churn)

In addition, we see that churners take on very similar distributions for features like Day Mins and Day Charge. That's not surprising as we'd expect minutes spent talking to correlate with charges. Let's dig deeper into the relationships between our features.


13. Now let’s look at how our features relate to one another



![](https://user-images.githubusercontent.com/36265995/102484259-45fd4480-4066-11eb-95e6-1f024b71bd62.png)
![](https://user-images.githubusercontent.com/36265995/102484275-4eee1600-4066-11eb-8490-b9a88a0a35a8.png)
![](https://user-images.githubusercontent.com/36265995/102484307-58777e00-4066-11eb-818d-d6bcfad98ff3.png)



We see several features that essentially have 100% correlation with one another. Including these feature pairs in some machine learning algorithms can create catastrophic problems, while in others it will only introduce minor redundancy and bias.



14. Let's remove one feature from each of the highly correlated pairs: Day Charge from the pair with Day Mins, Night Charge from the pair with Night Mins, Intl Charge from the pair with Intl Mins:



![](https://user-images.githubusercontent.com/36265995/102485088-6da0dc80-4067-11eb-9dc3-242468a8e5cf.png)



15. Now we will convert all the categorical variables using one hot encoding



![](https://user-images.githubusercontent.com/36265995/102485577-1bac8680-4068-11eb-8b10-ff06ab335b67.png)



16. We will split our data set into 3 channels: train, test, validation set:



![](https://user-images.githubusercontent.com/36265995/102485622-2830df00-4068-11eb-912a-2c010b48f9ce.png)


17. Now we will upload the final data into Amazon S3 bucket.


![](https://user-images.githubusercontent.com/36265995/102492092-6ed70700-4071-11eb-92ed-84204e4afa60.png)


18. Now quickly check the S3 bucket through the console to make sure you have uploaded the train.csv and validation.csv


![](https://user-images.githubusercontent.com/36265995/102492673-50bdd680-4072-11eb-8b61-c467b6911b84.png)

---

![](https://user-images.githubusercontent.com/36265995/102492689-574c4e00-4072-11eb-9638-cfdc09f2f3b3.png)


**Congratulations!!** You have successfully prepared the data to train an XGBoost model.

# Train & Tune the model

In this step, you will train your machine learning model with the training dataset, which you uploaded in Amazon S3 bucket in previous step.

1. First, we will specify XGBoost ECR container location.

![](https://user-images.githubusercontent.com/36265995/102494683-510ba100-4075-11eb-9842-f738b234108d.png)


2. Specify train and validation data set location:

![](https://user-images.githubusercontent.com/36265995/102495608-9381ad80-4076-11eb-849a-3d5a1b620f90.png)

3. Now, define the training parameter in SageMaker Estimator. You will also define the tuning hyperparameter and then call the “fit” method to train the model.

![](https://user-images.githubusercontent.com/36265995/102498294-10625680-407a-11eb-86c6-a8d90a07a332.png)

4. During the training process you have used AWS Spot instances. Look on logs to see how many saving did you make compareing to onDemand Instances.


> Training seconds: 41    
> Billable seconds: 15  
> Managed Spot Training savings: 63.4%  

5. Now, we will also check from AWS console to verify the training job finished.

![](https://user-images.githubusercontent.com/36265995/102504660-64246e00-4081-11eb-9baf-8e07d2250144.png)

**Congratulations!!** You successfully trained XGBoost model!!

# Deploy the model

In this step, you will deploy the trained model to a real-time HTTPS endpoint. This process can take around 6-8 min.  

**!!! If you can not use “_ml.m5.xlarge_” as you have limits and quatas on your AWS account please use “_ml.m5.large_”.**

![](https://user-images.githubusercontent.com/36265995/102501607-e9a61f00-407d-11eb-8c0d-aba4bfa220dc.png)

Now we will check AWS console view as well

![](https://user-images.githubusercontent.com/36265995/102505442-473c6a80-4082-11eb-9f55-2e521b40168a.png)

**Congratulations!!** You successfully deployed XGBoost model!!

# Inference the model with simple web page

In this step, you will inference the trained model throught simple web page that you will create.

1. At first open IAM service and go to Roles dashborad to create new role for lambda service.


![](https://user-images.githubusercontent.com/36265995/102611401-20883d80-412f-11eb-8a5c-f9da0a8d551b.png)

2. Select “_Create role_” and check Lamda service in “_Choose a use case_” section. Next, select “_Next: Permissions_” button.

![](https://user-images.githubusercontent.com/36265995/102612322-cee0b280-4130-11eb-9557-b58c668c86d6.png)

3. Select “_Create policy_”. The policy creator will open in new tab. Switch to JSON tab paste the following policy:

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Sid": "VisualEditor0",  
            "Effect": "Allow",  
            "Action": "sagemaker:InvokeEndpoint",  
            "Resource": "*"  
        }  
    ]  
}  
```
![](https://user-images.githubusercontent.com/36265995/102613161-4bc05c00-4132-11eb-8cfd-5f46083fe783.png)
