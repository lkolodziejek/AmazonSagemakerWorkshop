# Lab 3 - Amazon Sagemaker AutoPilot

In this lab, you will get hands-on with Amazon Sagemaker AutoML. An automated machine learning (commonly referred to as AutoML) solution for tabular datasets. You can use SageMaker Autopilot in different ways: on autopilo (hence the name) or with human guidance, without code through SageMaker Studio, or using the AWS SDKs.

Losing customers is costly for any business. Identifying unhappy customers early on gives you a chance to offer them incentives to stay. This lab describes using machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. We will use the same data set as we did in **_Lab 1_** as we are already familiar with it.


In this lab SageMaker Autopilot first inspects your data set, and runs a number of model candidates to figure out the optimal combination of data preprocessing steps, machine learning algorithms and hyperparameters. It then uses this combination to train an Inference Pipeline, which you can easily deploy either on a real-time endpoint, or use it for batch processing.  
  
  
- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#setup)
- [_Data_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%203/README.md#data)

  
**Ok, lest start the lab!!**

# Setup

1. We will start with opening Notebook `autopilot_customer_churn.ipynb` in “AmazonSagemakerWorkshop/Lab 3” folder. We will skip detailed instruction how to procees as you are the expert now.  
  
  **Zdjęcie tutaj, jak wygląda katalog Lab 3!**
    
In case You did not follow this workshi in order, you can find detailed instruction how to complete this step [_“here”_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%201/README.md#data-preparation).
  
  
2. In the very first two cells we will start with specifying:  
  
- The S3 bucket and prefix that you want to use for training and model data. Replace the appropriate variable names according to your preferences.  
   
  
![ReplaceMe](https://user-images.githubusercontent.com/36265995/102872824-926aca80-4440-11eb-8998-00b87665ceb3.png)  
  
  
- Next, we'll import the Python libraries we'll need for the remainder of the exercise. Execute the first two cells by pressing `Shift`+`Enter` in each of the cells.  
  
![Import](https://user-images.githubusercontent.com/36265995/102874970-7caad480-4443-11eb-8c62-c6a9de42db1c.png)  
  

# Data

In this section we will dowload the data set. We are going to use the same data set as we did in **_Lab 1_** as we are already familiar with it. Just to briefly recap the dataset we use is publicly available and was mentioned in the book [Discovering Knowledge in Data](https://www.amazon.com/dp/0470908742/) by Daniel T. Larose. It is attributed by the author to the University of California Irvine Repository of Machine Learning Datasets.

3. Let's download that dataset now:  
  
  
![Download](https://user-images.githubusercontent.com/36265995/102876391-67cf4080-4445-11eb-9c9a-fb353ec878d1.png)


4. Read the data into a Pandas data frame and take a look

It is important to keep in mind that it is good practice to check the dataset to make sure that it has no obvious errors. The Autopilot process can take long time to complete, to inspect the dataset before you start a job.   

[LoadData](https://user-images.githubusercontent.com/36265995/102878913-496b4400-4449-11eb-8bff-5a0a844a733a.png)

It shouldn't be a surprise that we end up with the same output as we did in **_Lab 1_**. We will skip the where we analyze the data set. We want Amazon Sagemaker Autopilot to inspect our data set, and runs a number of model candidates to figure out the optimal combination of data preprocessing steps. Still we need to divide the data into training and testing splits.

5. Divide the data into training and testing splits.  
  
  
![Split](https://user-images.githubusercontent.com/36265995/102880525-be3f7d80-444b-11eb-872f-ba86a28060e7.png)
  
  
  






