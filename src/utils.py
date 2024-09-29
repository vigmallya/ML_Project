import os
import sys

import numpy as np 
import pandas as pd
import pickle #Helps to create pickle file
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

#For creating pickle file
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

#Evaluating models and returns list of models with its prediction rate.
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model_param= param[list(models.keys())[i]]

            #intialise GridSearchCV
            gs = GridSearchCV(model,model_param,cv=3)

            #gs.fit(X_train,y_train) Performs the search over the hyperparameters in model_param on the training data (X_train, y_train) using cross-validation.
            #GridSearchCV trains the model multiple times using different sets of parameters and evaluates each configuration with cross-validation.
            gs.fit(X_train,y_train)

            #gs.best_params_ returns the best hyperparameters found by GridSearchCV
            #Update(set_params) the model with the best parameters found
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) # Train the model with best paramter found by GridSearchCV

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    

    except Exception as e:
        raise CustomException(e, sys)