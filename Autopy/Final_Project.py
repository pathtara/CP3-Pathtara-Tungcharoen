import pandas as pdr
import datetime
pttgc = pdr.get_data_yahoo('PTTGC.BK', 
                          start=datetime.datetime(2017, 10, 1), 
                          end=datetime.datetime(2017, 12, 30))