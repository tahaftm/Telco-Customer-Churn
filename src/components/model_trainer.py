from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from dataclasses import dataclass
import os
from src.utils import evaluate_model
from src.exception import CustomException
from src.logger import logging
import sys
from src.utils import save_object
from sklearn.metrics import accuracy_score

@dataclass
class ModelTrainingConfig:
    model_trained_path = os.path.join("artifacts", "model.pkl")

class ModelTraining:
    def __init__(self):
        self.model_training_path= ModelTrainingConfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "KNN": KNeighborsClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "XGBoost": XGBClassifier(),
                "CatBoost": CatBoostClassifier(verbose=0),
                "SVM": SVC(),
                "Naive Bayes": GaussianNB(),
            }

            params = {
            "Logistic Regression": {},

            "KNN": {
                "n_neighbors": [3, 5, 7, 9],
                "weights": ["uniform", "distance"],
                "metric": ["euclidean", "manhattan"]
            },

            "Decision Tree": {
                "max_depth": [None, 5, 10, 20],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4]
            },

            "Random Forest": {
                "n_estimators": [100, 200],
                "max_depth": [None, 10, 20],
                "min_samples_split": [2, 5],
                "min_samples_leaf": [1, 2]
            },

            "XGBoost": {
                "n_estimators": [100, 200],
                "learning_rate": [0.01, 0.1, 0.2],
                "max_depth": [3, 5, 7],
                "subsample": [0.8, 1.0],
                "colsample_bytree": [0.8, 1.0]
            },

            "CatBoost": {
                "iterations": [100, 200],
                "learning_rate": [0.01, 0.1],
                "depth": [4, 6, 8]
            },

            "SVM": {
                "C": [0.1, 1, 10],
                "kernel": ["linear", "rbf"],
                "gamma": ["scale", "auto"]
            },

            "Naive Bayes": {
                "var_smoothing": [1e-9, 1e-8, 1e-7]
            },
        }
            
            model_report:dict = evaluate_model(X_train,y_train,X_test, y_test, models,params)
            accuracy_arr = []
            for i in model_report.items():
                accuracy = i[1]
                accuracy_arr.append(accuracy)

            max_r2_score= max(accuracy_arr)
            if max_r2_score<0.6:
                raise CustomException("No best model found")
            for key,value in model_report.items():
                if value  == max_r2_score:
                    model_name = key
            model = models[model_name]
            logging.info(f"Best found model on both training and testing dataset")
            save_object(
                file_path=self.model_training_path.model_trained_path,
                obj=model
            )
            predicted=model.predict(X_test)
            accuracy_test = accuracy_score(y_test, predicted)
            print(accuracy_test)
        except Exception as e:
            raise CustomException(e,sys)