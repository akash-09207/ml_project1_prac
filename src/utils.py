import os,sys
import dill

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from src.exception import CustomException

def save_object(file_path,object):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(object,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(x_train,y_train,x_test,y_test,models):
    report={}
    for model in models.items():
        mod=model[1]
        mod.fit(x_train,y_train)
        y_pred=mod.predict(x_test)
        score=r2_score(y_test,y_pred)
        report[model[0]]=score
    return report
