import pandas as pd
import numpy as np
e_d = {'name': ['Anestisea','Dima','Katherine','James','Emily','Michal','Mattew','Laura','Kevin','Jonas'],
       'score':[12.5,9,16.5,15,18,14,10,8,np.nan,9],
       'attempts':[1,2,3,4,5,1,2,3,4,5],
       'qulify':['yes','no','no','no','no','no','no','no','yes','yes']}
lables = ['a','b','c','d','e','f','g','h','j','i']
df = pd.DataFrame(e_d, index= lables)
print(df.info())