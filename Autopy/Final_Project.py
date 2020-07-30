#Business Strategic Analysis
import pandas as pd
from pandas_datareader import data
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline
#config InlineBackend.figure_format='retina'


df = data.DataReader('kbank.bk', data_source='yahoo', start='2017-01-01')
x = sns.lineplot(x=df.index, y='Adj Close', data=df)

print(x)





class main_windows:
    def register():
        pass


    def login():
        pass
        
class change:
    def test():
        pass
#test











