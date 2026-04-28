import os
import sys
import pickle

from sklearn.metrics import r2_score



import dill
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # <-- this line must exist
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)


    
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:        
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)  # Train the model
            y_test_pred = model.predict(X_test)  # Predict on test data
            test_model_score = r2_score(y_test, y_test_pred)  # Calculate R2 score
            report[list(models.keys())[i]] = test_model_score  # Store the score in the report
        return report   

    except Exception as e:
        raise CustomException(e, sys)
