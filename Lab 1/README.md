# Lab 1

**Feature Engineering, Training (using built in algorithm - XGBoost), Deployment, Inferention**

In this lab, you will learn how to use Amazon SageMaker to build, train, and deploy a machine learning (ML) model. We will use the popular XGBoost ML algorithm for this exercise. Amazon SageMaker is a modular, fully managed machine learning service that enables developers and data scientists to build, train, and deploy ML models at scale.

Taking ML models from concept to production is typically complex and time-consuming. You have to manage large amounts of data to train the model, choose the best algorithm for training it, manage the compute capacity while training it, and then deploy the model into a production environment. Amazon SageMaker reduces this complexity by making it much easier to build and deploy ML models. After you choose the right algorithms and frameworks from the wide range of choices available, Amazon SageMaker manages all of the underlying infrastructure to train your model at petabyte scale, and deploy it to production.

In this lab, you will assume the role of a machine learning developer. Your task is to identify unhappy customers early on to have a chance to offer them incentives to stay. Losing customers is costly for any business. You will use notebook `xgboost_customer_churn.ipynb` that describes how to use machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. ML models rarely give perfect predictions though, so this notebook is also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.


- [_Data Preparation_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#data-preparation)
- [_Train & Tune the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#train--tune-the-model)
- [_Deploy the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#deploy-the-model)
- [_Inference the model with simple web page_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#inference-the-model-with-simple-web-page)


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
This policy will allow a lambda function to make inferance on the model we have created and deployed in Amazon SageMaker.

![](https://user-images.githubusercontent.com/36265995/102613161-4bc05c00-4132-11eb-8cfd-5f46083fe783.png)

4. Select “_Review policy_” and provide name and describtion for it.

![](https://user-images.githubusercontent.com/36265995/102613984-b756f900-4133-11eb-83f1-5e23895a27da.png)

5. Select “_Create policy_” and go back to “_Create role_” tab you have been on. Search you policy and mark it.

![](https://user-images.githubusercontent.com/36265995/102614420-7c08fa00-4134-11eb-9100-6834bcf7b1ac.png)

6. Select “_Next: Tags_”, “_Next: Review_” and provide name for the role.

![](https://user-images.githubusercontent.com/36265995/102614685-f5a0e800-4134-11eb-97ab-434ce317c1aa.png)

7. Select “_Create role_”.

8. As we have just created a role, now we can set up a lambda function that will handle the request from web page and pass it to the ML model hosted on Amazon SageMaker. Go to AWS Lambda Service dashboard and select “_Create function_”

![](https://user-images.githubusercontent.com/36265995/102624271-0efd6080-4144-11eb-9e0b-f68db1dc84c1.png)

9. Provide a name for your lambda functiony and select **_Python 3.7_** as runtime. Next, expand “_Change default execution role_” in “_Permissions_” section. Select “_Use an existing role_” and select the role you created few steps earlier. Finally select “_Create function_”

![](https://user-images.githubusercontent.com/36265995/102625458-d199d280-4145-11eb-96a4-638fb7756a18.png)

10. Now, copy the content of the `xgboost-customerchurn-ep-invoker-lambda.py` file into lambda code editor.

In the line 8 `ENDPOINT_NAME` environment variable was defined. This is the name of the Amazon Sagemaker endpoint that we created while deploying the model. To get this endpooint name please go back to section [_Deploy the model_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#deploy-the-model) where you can find it. In this case the neme is: `sagemaker-xgboost-2020-12-17-14-26-01-562`.

![](https://user-images.githubusercontent.com/36265995/102627384-6bfb1580-4148-11eb-94d1-b2c1b3b4aabd.png)

11. While we have identified the name of the Amazon Sagemaker endpoint that we created we need to configure environment variable `ENDPOINT_NAME`. Scroll down the AWS Lambda page to find “_Environment variables_”. Click “_Edit_”.

![](https://user-images.githubusercontent.com/36265995/102628639-4b33bf80-414a-11eb-9a80-f3ee942a69af.png)

12. Select “_Add environment variable_”. Provide Key `ENDPOINT_NAME` and the value that you identified in step 10. Please keep in mind that your value will be differnet then value presented here. Click “_Save_”

![](https://user-images.githubusercontent.com/36265995/102629134-06f4ef00-414b-11eb-8dea-153156b1e5c2.png)

13. You are now ready do deploy your function. Scroll up to the top of lambda code editor. In the top right corner select “_Deploy_”

![](https://user-images.githubusercontent.com/36265995/102627384-6bfb1580-4148-11eb-94d1-b2c1b3b4aabd.png)

14. It is time to share our lambda function with others. To do this we will use Amazon API Gateway.

Scroll up to the top of the page. Here you will find graphical designer that makes it easier to add lambda triggers and destinations. Click on “_+ Add trigger_” icon. This will open “_Trigger configuration_” page.

![](https://user-images.githubusercontent.com/36265995/102633979-7a016400-4151-11eb-97b7-178a94267b54.png)

14. Please fill “_Trigger configuration_” page as follow, than select “_Add_”

![](https://user-images.githubusercontent.com/36265995/102634407-14fa3e00-4152-11eb-8f79-903362c55035.png)

The “_Designer_” section now looks like this:

![](https://user-images.githubusercontent.com/36265995/102635048-082a1a00-4153-11eb-86de-b126b7a2a9b9.png)

Also the new section “_API Gateway_” has appeard. Expand the “_Details_” arrow to get the https endpoint address where your lambda function will be exposed. Please keep in mind that your https address will be diferent. Copy the address as we will need it while creating our web page.

![](https://user-images.githubusercontent.com/36265995/102635755-0ca30280-4154-11eb-9396-6ae239d355a7.png)

15. Finally we can create our simple web page to have more user friendy interface to inference our ML model.

We star with the the file `xgboost-customerchurn-website.html`. This is very simple html file that creates simple form with the input for vector of features that ML model required. Please open the html source code. In 8th line `endpoint` variable is defined. Use https endpoint address that we copied in previous step and assign it to this variable.

![](https://user-images.githubusercontent.com/36265995/102639353-39a5e400-4159-11eb-937e-07953cf21145.png)

16. Now it is time to set up and deploy our web page.

We will use Amazon S3 service to host our web page. To keep this it as simple as possible we will reuse a S3 bucket that we have created at the very beginning of this lab. We have created bucket within notebook `xgboost_customer_churn.ipynb` by replacing the `REPLACE_ME` string with desired name.

![](https://user-images.githubusercontent.com/36265995/102475949-ce75e800-405a-11eb-935e-636c0be8cf3d.png)

Please open Amazon S3 service dashbord and go the bucket you have created.

![](https://user-images.githubusercontent.com/36265995/102661586-6b30a680-417d-11eb-9358-9fb4c54b8bec.png)

17. Select “_Permissions_” tab and then “_Edit_” button in “_Block public access (bucket settings)_”:

![](https://user-images.githubusercontent.com/36265995/102661910-06c21700-417e-11eb-80aa-34e70882fb08.png)

You have to confirm that by writing `confirm` and clicking “_Confirm_”.

![confirm](https://user-images.githubusercontent.com/36265995/102662312-e34b9c00-417e-11eb-8a42-1dbc1273e735.png)

18. Unmark “_Block all public access_” and click “_Save changes_”

![](https://user-images.githubusercontent.com/36265995/102662066-5d2f5580-417e-11eb-9c56-f6c8b77370a8.png)

19. Select “_Upload_” and and `xgboost-customerchurn-website` to the bucket. Leave all parameters as default.
