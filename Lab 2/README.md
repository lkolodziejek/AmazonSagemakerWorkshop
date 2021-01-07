
## Lab 2

**Feature Engineering, Training (using your own scikit-learn scripts), Deployment, Inferention**

In this lab we will learn how to use our own Scikit-learn scripts with Amazon Sagemaker. Scikit-learn is a very popular Python machine learning framework. Scikit-learn is very popular becouse of its well-designed API and number of different algorithms for classification, regression, clustering, dimensionality reduction, and data/feature pre-processing as well.

In this lab, you will assume the role of a machine learning developer. Your task is to classify different types of irises . You will use notebook `Scikit-learn Estimator Example With Batch Transform.ipynb` that describes how to use machine learning (ML) for the automated classification of irises (Setosa, Versicolour, and Virginica). The main different between ***lab 2*** and ***lab 1*** is that here you will bring your own Scikit-learn scripts and Amazon Sagemaker will provide pre-built container with the framework image.

- [_Setup_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#setup)
- [_Data_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#data)
- [_Scikit-learn script_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#scikit-learn-script)
- [_Create and run Amazon Sagemaker Scikit-learn estimator_](https://github.com/pawelmoniewski/AmazonSagemakerWorkshop/blob/main/Lab%202/README.md#create-and-run-amazon-sagemaker-scikit-learn-estimator) 


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

Now we are ready to run scikit-learn script using Amazon Sagemaker. More precisely we will use `SKLearn` estimator which support number of helpful environment variables to access properties of the training environment, such as:

- `SM_MODEL_DIR`: A string representing the path to the directory to write model artifacts to. Any artifacts saved in this folder are uploaded to S3 for model hosting after the training job completes.
- `SM_OUTPUT_DIR`: A string representing the filesystem path to write output artifacts to. Output artifacts may include checkpoints, graphs, and other files to save, not including model artifacts. These artifacts are compressed and uploaded to S3 to the same S3 prefix as the model artifacts.
- `SM_CHANNEL_TRAIN`: A string representing the path to the directory containing data in the 'train' channel.
- `SM_CHANNEL_TEST`: Same as above, but for the 'test' channel.

A typical training script loads data from the input channels, configures training with hyperparameters, trains a model, and saves a model to model_dir so that it can be hosted later. Hyperparameters are passed to your script as arguments and can be retrieved with an argparse.ArgumentParser instance. For example, the script that we will run in this notebook is the below:

```python
from __future__ import print_function

import argparse
import joblib
import os
import pandas as pd

from sklearn import tree


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyperparameters are described here. In this simple example we are just including one hyperparameter.
    parser.add_argument('--max_leaf_nodes', type=int, default=-1)

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    raw_data = [ pd.read_csv(file, header=None, engine="python") for file in input_files ]
    train_data = pd.concat(raw_data)

    # labels are in the first column
    train_y = train_data.iloc[:, 0]
    train_X = train_data.iloc[:, 1:]

    # Here we support a single hyperparameter, 'max_leaf_nodes'. Note that you can add as many
    # as your training my require in the ArgumentParser above.
    max_leaf_nodes = args.max_leaf_nodes

    # Now use scikit-learn's decision tree classifier to train the model.
    clf = tree.DecisionTreeClassifier(max_leaf_nodes=max_leaf_nodes)
    clf = clf.fit(train_X, train_y)

    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf
```

# Create and run Amazon Sagemaker Scikit-learn estimator

As it was mentioned in previous section we can run Scikit-learn training script using `SKLearn` (sagemaker.sklearn.estimator.sklearn) estimator. It accepts several constructor arguments:

- ***entry_point***: The path to the Python script SageMaker runs for training and prediction.
- ***role***: Role ARN
- ***train_instance_type*** (optional): The type of SageMaker instances for training. Note: Because Scikit-learn does not natively support GPU training, Sagemaker Scikit-learn does not currently support training on GPU instance types.
- ***sagemaker_session*** (optional): The session used to train on Sagemaker.
- ***hyperparameters*** (optional): A dictionary passed to the train function as hyperparameters.

1) Now we can construct `SKLearn` estimator with the following code:  
  
  
  ![Estimator](https://user-images.githubusercontent.com/36265995/103889072-15994b00-50e6-11eb-92be-011c9b96ed8b.png)
  
  
2) And finally we can run training by calling `fit` on the estimator.

The following code will start an Amazon Sagemaker training job that will download the data for us, invoke our scikit-learn code (in the provided script file), and save any model artifacts that the script creates.


