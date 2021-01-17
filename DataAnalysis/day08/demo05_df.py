"""
    dateframe
"""
import numpy as np
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',14]]
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index=['AID01','AID02','AID03'],columns=['Name','Age'])
print(df)