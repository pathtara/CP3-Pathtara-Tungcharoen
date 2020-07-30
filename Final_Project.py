#Business Strategic Analysis
import pandas as pd
#from sklearn import *
import seaborn as sns
import matplotlib.pyplot as plt
import firebase_admin
import requests
from pandas_datareader import data
from firebase_admin import credentials
from firebase_admin import db
from bs4 import BeautifulSoup as bs




class FireBase:
    def firebase_login():
        cred = credentials.Certificate(
            'python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json'
            )
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://python3-born2dev.firebaseio.com'
            })
        

class main_window:
    def register():
        user_data = db.reference('Users').get()
        while True:
            user_input = str(input("Username: "))
            if user_input in user_data.keys():
               print("Username alreadys exists, please try the different one.")
               True
            else:               
                break
        while True:                            
            password_input_1 = str(input("Password: "))
            password_input_2 = str(input("Confirm password: "))            
            if password_input_1 == password_input_2:
                break
            else:
                print("Password and confirm password did not match. Please try again.")            
        first_name = str(input("First name: "))
        last_name = str(input("Last name: "))
        age = int(input("Age: "))  # Only number can be inputed
        ref = db.reference('Users')
        user_ref = ref.child(user_input)
        user_ref.set({
            'password': password_input_1,
            'firstname': first_name,
            'lastname': last_name,
            'age': age  
            })                                                
        print("Registier Complete.")
        
            
                    
    def login():
        user_data = db.reference('Users').get()
        for i in range(0, 5):
            username = str(input("Username : "))
            password = str(input("Password : "))
            try:
                if username in (user_data.keys()) and password == str(user_data[username]['password']):
                    print("Login Success")
                    break
                else:
                    pass
            except KeyError:
                pass
            print("Incorrect username or password. Please try again.")
            print("You can try in %d times" % (4 - i))
            print("")
        main_window.exit_program()
        # back to main menu
                                        

    ### Menu
    def main_forex():
        pass
        
        
    def main_equity():
        pass 
        
        
    def exit_program():
        print("Thank you".center(40, "-"))    
        

class Forex:
    pass

        
class Equity:
    def get_quote():
        pass
    
    df = data.DataReader('BANPU.bk', data_source='yahoo', start='2015-01-01', end= '2020-07-29')

    def fundamental_matric(soup, metric):
        return soup.find(text = metric).find_next(class_='snapshot-td2').text
        
        
    def get_fundaamental_data(df):
        for symbol in df.index:
            try:
                url = ("http://finviz.com/quote.ashx?t" + symbol.lower())        
                soup = bs(requests.get(url).content)
                for m in df.columns:
                    df.loc[symbol, m] = fundamental_metric(soup, m)
            except Exception as e:
                print (symbol, 'not found')
        return df            
        

#FireBase.firebase_login()
#main_window.register()
#main_window.login()