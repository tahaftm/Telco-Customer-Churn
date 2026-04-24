import os
import dill
from src.exception import CustomException
import sys

def save_object(file_path, obj):
    try:
        folder_name = os.path.dirname(file_path)
        os.makedirs(folder_name, exist_ok=True)
        with open(file_path, "wb") as f:
            dill.dump(obj, f)
    except Exception as e:
        raise CustomException(e,sys)