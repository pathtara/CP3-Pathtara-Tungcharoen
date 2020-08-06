#Business Strategic Analysis
import pandas as pd
from pandas_datareader import data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_datareader.yahoo.daily
#matplotlib inline
#config InlineBackend.figure_format='retina'

a = [1,2,3]
b = [7,8,9]

df = data.DataReader('PTT', data_source='yahoo', start='2017-01-01')
df2=data.NaverDailyReader(symbols='kbank.bk',start='2017-01-01')

#x = sns.lineplot(x=df.index, y='Adj Close', data=df)

print(df.head(2))


print(df2)

class main_windows:
    def register():
        pass


    def login():
        pass
        
class change:
    def test():
        pass
#test











