import pandas as pd
from dataclasses import dataclass
import os
from src.exception import CustomException
import sys
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.preprocessor_path = DataTransformationConfig()
    def get_preprocessor_obj():
        try:
            numerical_features = ["customerID"]
        except Exception as e:
            raise CustomException(e,sys)
        
