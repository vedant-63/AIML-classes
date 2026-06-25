import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

from numpy import dtypes

wr.filterwarnings('ignore')

df=pd.read_csv("data_dictionary.csv")
#print(df.head())
#print(df.shape())
#print(df.describe().T)
#print(df.isnull().sum())
# print(df.columns)
# print(dtypes)
