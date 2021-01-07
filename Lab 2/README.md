
## Lab 2

**Feature Engineering, Training (using your own scikit-learn scripts), Deployment, Inferention**

In this lab we will learn how to use our own Scikit-learn scripts with Amazon Sagemaker. Scikit-learn is a very popular Python machine learning framework. Scikit-learn is very popular becouse of its well-designed API and number of different algorithms for classification, regression, clustering, dimensionality reduction, and data/feature pre-processing as well.

In this lab, you will assume the role of a machine learning developer. Your task is to classify different types of irises . You will use notebook `Scikit-learn Estimator Example With Batch Transform.ipynb` that describes how to use machine learning (ML) for the automated classification of irises (Setosa, Versicolour, and Virginica). The main different between ***lab 2*** and ***lab 1*** is that here you will bring your own Scikit-learn scripts and Amazon Sagemaker will provide pre-built container with the framework image.

- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#setup)
- [_Data_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#data)
- [_Scikit-learn script_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#setup)

***Ok, lest start the lab !!!***

# Setup

1. Ok, let's open `Scikit-learn Estimator Example With Batch Transform.ipynb` notebook in “AmazonSagemakerWorkshop/Lab 3” folder. We will skip detailed instruction how to procees as you are the expert now. You should see the following files in Amazon Sagemaker Studio:  
  
  
![Files](https://user-images.githubusercontent.com/36265995/103879078-a61c5f00-50d7-11eb-9ccd-2aeb6c607221.png)
  
  
In case You did not follow this workshop in order, you can find detailed instruction how to complete this step [_here_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#data-preparation) (step 1 to 5).
  
  
2. Now run first cell with the basic setup instructions you are already familiar with:
  
  
  ![FirstCell](https://user-images.githubusercontent.com/36265995/103879971-cf89ba80-50d8-11eb-916b-43e57c9bb3e8.png)
  
  
# Data

When training large models with huge amounts of data, you'll typically use big data tools, like Amazon Athena, AWS Glue, or Amazon EMR, to create your data in S3. For the purposes of this example, we're using a sample of the classic [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), which is included with Scikit-learn. We will load the dataset, write locally, then write the dataset to s3 to use.

1. Let's load the data localy to `iris.csv` file:
  
  
  ![Data](https://user-images.githubusercontent.com/36265995/103880681-c0efd300-50d9-11eb-9924-f9b7ed08ec8f.png)
  
  
2. Now we will create a default S3 bucket and upload a dataset.

In lab 1 we _a priori_ declare the name of the bucket we want to create. This is perfectly fine. Still with Amazon Sagemaker Python SDK you can create a default bucket. This mean that the name will be generated automatically for you. Here is the code:
  
  
  ![S3](https://user-images.githubusercontent.com/36265995/103881447-bd108080-50da-11eb-8009-6e240446314b.png)
  
  
3. Verify if the default S3 bucket was created for you:

In my case it is: `sagemaker-eu-west-1-526743947142`.  
  
  ![S3](https://user-images.githubusercontent.com/36265995/103882149-ad456c00-50db-11eb-9136-349894df0a4b.png)
  
  
  
# Scikit-learn script
