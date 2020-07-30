
# For data manipulation
import pandas as pd

# To extract fundamental data
from bs4 import BeautifulSoup as bs
import requests

def fundamental_metric(soup, metric):
    return soup.find(text = metric).find_next(class_='snapshot-td2').text
    
def get_fundamental_data(df):
    for symbol in df.index:
        try:
            url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
            soup = bs(requests.get(url).content) 
            for m in df.columns:                
                df.loc[symbol,m] = fundamental_metric(soup,m)                
        except Exception as e:
            print (symbol, 'not found')
    return df
    
stock_list = ['AMZN','GOOG','PG','KO','IBM','DG','XOM','KO','PEP','MT','NL','GSB','LPL']

metric = ['P/B',
'P/E',
'Forward P/E',
'PEG',
'Debt/Eq',
'EPS (ttm)',
'Dividend %',
'ROE',
'ROI',
'EPS Q/Q',
'Insider Own'
]


df = pd.DataFrame(index=stock_list,columns=metric)
df = get_fundamental_data(df)
df

df['Dividend %'] = df['Dividend %'].str.replace('%', '')
df['ROE'] = df['ROE'].str.replace('%', '')
df['ROI'] = df['ROI'].str.replace('%', '')
df['EPS Q/Q'] = df['EPS Q/Q'].str.replace('%', '')
df['Insider Own'] = df['Insider Own'].str.replace('%', '')
df = df.apply(pd.to_numeric, errors='coerce')
df


df_filtered = df[(df['P/E'].astype(float)<15) & (df['P/B'].astype(float) < 1)]
df_filtered

df_filtered = df_filtered[df_filtered['EPS Q/Q'].astype(float) > 10]
df_filtered


df = df[df['Insider Own'].astype(float) > 30]
df
