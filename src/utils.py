import os
import sys
import pickle
import logging



import dill
import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # <-- this line must exist
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)


    except Exception as e:
        raise CustomException(e, sys)