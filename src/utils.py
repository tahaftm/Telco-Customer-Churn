import os
import dill
from src.exception import CustomException
import sys
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def save_object(file_path, obj):
    try:
        folder_name = os.path.dirname(file_path)
        os.makedirs(folder_name, exist_ok=True)
        with open(file_path, "wb") as f:
            dill.dump(obj, f)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models:dict, params:dict):
    report = {}
    for i in models.items():
        name = i[0]
        model = i[1]
        model.fit(X_train,y_train)
        parameters = params[name]
        gm = GridSearchCV(model,cv= 3,param_grid=parameters)
        gm.fit(X_train,y_train)
        test_pred= gm.predict(X_test)
        accuracy = accuracy_score(y_test, test_pred)
        report[name] = accuracy
    return report

def load_object(path):
    try:
        with open(path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        CustomException(e,sys)