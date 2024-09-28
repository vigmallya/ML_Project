import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer #To create pipeline 
from sklearn.impute import SimpleImputer #For handling missing value, we can use different imputation techniques as well
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path= os.path.join("artifacts","preprocessor.pkl")  

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    #To create pickle file and data transformation
    #Creates and returns a preprocessing pipeline that handles missing values, encoding, and scaling for both numerical and categorical columns.
    def get_data_transformer_obj(self):
        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            numerical_pipeline= Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="median")), #Missing values will be replaced by median value
                ("scaler", StandardScaler())
            ])
            
            categorical_pipeline=Pipeline(
                steps= [
                ("imputer", SimpleImputer(strategy="most_frequent")), #Missing values will be replaced by mode value
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])
            
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            #Combination of Numerical and Categorical pipeline
            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read Train and Test Data completed")
            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_obj()

            target_column_name="math_score"
            #Consider train and test dataset
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            #combining input and target datasets
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            #Create pickel file to reuse it for future steps without rebuilding it.
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)