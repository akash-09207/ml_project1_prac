import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

x={'A':[10,20,30,np.nan,50],'B':[1,np.nan,3,4,5]}

df=pd.DataFrame(x)
print(df)

p=ColumnTransformer([
    ('imputer1',SimpleImputer(strategy='mean'),['B','A']),
      
])

x=p.fit_transform(df)
print(x)