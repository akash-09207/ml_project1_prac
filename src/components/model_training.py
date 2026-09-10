import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_tariner_config=ModelTrainerConfig()
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Splitting Tarining and test Inputs data')
            x_train,y_train,x_test,y_test=(train_array[:,:-1],train_array[:,-1],
                                                          test_array[:,:-1],test_array[:,-1])
            models={
                'Random Forest':RandomForestRegressor(),
                'Decision Tree':DecisionTreeRegressor(),
                'GradientBossting':GradientBoostingRegressor(),
                'LinearRegressor':LinearRegression(),
                'KNNeighbours':KNeighborsRegressor(),
                'XGBClassifier':XGBRegressor(),
                'Catboosting regressor':CatBoostRegressor(verbose=False),
                'Adaboost regressor': AdaBoostRegressor()
            }
            model_report:dict=evaluate_model(x_train,y_train,x_test,y_test,models)

            best_model_score=max(model_report.values())
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException('No Best Model Found')
            logging.info('Best Model found on Test data')

            save_object(
                file_path=self.model_tariner_config.trained_model_file_path,
                object=best_model
            )
            return best_model_score,best_model_name
        except Exception as e:
            raise CustomException(e,sys)