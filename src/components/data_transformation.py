import pandas as pd
from dataclasses import dataclass
import os
from src.exception import CustomException
import sys
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object
from src.logger import logging
import numpy as np

@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.preprocessor_path = DataTransformationConfig()
    def get_preprocessor_obj(self):
        try:
            numerical_features = ['tenure', 'MonthlyCharges','TotalCharges']
            categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

            num_pipe = Pipeline([
                ("StandardScaler",StandardScaler()),
            ])
            cat_pipe = Pipeline([
                ("onehot",OneHotEncoder()),
            ])
            preprocessor = ColumnTransformer([
                ("num_pipe", num_pipe, numerical_features),
                ("cat_pipe", cat_pipe, categorical_features)
            ])
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_preprocessing(self, train_path, test_path):
        try:
            train_arr = pd.read_csv(train_path)
            test_arr = pd.read_csv(test_path)
            
            logging.info("Reading training and testing data")

            target = "Churn"
            train_arr_without_target = train_arr.drop([target], axis = 1)
            test_arr_without_target = test_arr.drop([target], axis = 1)

            train_arr_target = train_arr[target]
            test_arr_target = test_arr[target]

            logging.info("Applynig preprocessing object")
            preprocessor = self.get_preprocessor_obj()
            save_object(file_path = self.preprocessor_path.preprocessor_path, obj = preprocessor)
            preprocessed_train_arr =preprocessor.fit_transform(train_arr_without_target)
            preprocessed_test_arr = preprocessor.transform(test_arr_without_target)
            train_arr = np.c_[preprocessed_train_arr,train_arr_target]
            test_arr = np.c_[preprocessed_test_arr,test_arr_target]
            logging.info("Preprocessed training and testing data saved")

            return(
                train_arr,
                test_arr,
                self.preprocessor_path.preprocessor_path
            )
        except Exception as e:
            raise CustomException(e,sys)        

            

