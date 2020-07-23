
from forex_python.converter import *
import math as m 
from datetime import datetime

c = CurrencyRates()

class UserData:
    id = "admin"
    password = "1234"
    
    
class Product:
    
    product_list = []
    product_quantity = 0
    
    def add_product_quantity():
        price = 0
        try:
            Product.product_quantity = int(input("How many products did you wish to calculate? : "))
            print("")
        except:
            print("Only number can be inputed!!!")
            print("")
            return Product.add_product_quantity()
        if Product.product_quantity <= 0:
            print("Number inputed must more than zero. Please try again!!!")
            print("")
            return Product.add_product_quantity()
        return Product.add_product_list()
            
            
    def add_product_list():
        i = 0
        currency = str(input("Please enter your product's currency code : "))
        currency_2 = set(currency.upper() for currency in ExchangeRate.ccy)
        while True:
            if currency.upper() in currency_2:
                break
            else:
                print("Currency not found. Please try again!!!")
                print("")
                return Product.add_product_list()            

        print("")
        i = 0    
        for i in range(0, Product.product_quantity):
           print("Product no.", i+1) 
           product = str(input("Name :"))
           try:
               price = float(input("Price : "))
               print("")
           except:
               print("Only Number can be inputed!!!")
               print("Please re-enter product's name and price.")
               print("")
               return Product.add_product_list()
           Product.product_list.append([product, price, currency.upper()]) 
        return Calculator.calculate()              


class ExchangeRate:
    
    user_rate = 0
    ccy = list(c.get_rates("THB").keys())
   
    
    def exchange_rate_list():
        print("Exchange rate Data as of ", datetime.now())
        print("_" * 40)
        print("")
        i = 0
        rate = ""
        ccy = ExchangeRate.ccy
        for i in range(len(ccy)):
            rate = round(c.get_rate(ccy[i], 'THB'), 4)
            print("%s / THB          %f" % (ccy[i], rate))
        print("_" * 40)
        print("")
        return Main.menu_selected()
        
    def user_exchange_rate():
        ccy = Product.product_list[0][2]                
        ExchangeRate.user_rate = round(c.get_rate(ccy, 'THB'), 4)
        print("Exchange rate for %s / THB = %f" % (ccy, ExchangeRate.user_rate))                
        print("")
        
        
class Calculator:        
    
    total_price_foreign = 0
    total_price_THB = 0
    duty_rate = 0.10 #estimate 10%
    duty = 0 
    vat = 0
    
    def calculate():
        print("Import Duty Calculator")
        print("_" * 40)
        print("")
        Calculator.total_product_list()
        ExchangeRate.user_exchange_rate()
        Calculator.total_price_THB = Calculator.total_price_foreign * ExchangeRate.user_rate
        print("Total in THB :             THB", round(Calculator.total_price_THB), 2)
        Calculator.tax_calculate()
        print("Duty", " " * 21, "THB", Calculator.duty)
        print("VAT (7%)", " " * 17, "THB", Calculator.vat)
        net_price = Calculator.total_price_THB + Calculator.vat + Calculator.duty
        print("")
        print("Net Price :", " " * 14, "THB", round(net_price, 2))
        print("_" * 40)
        print("")
        Product.product_list = []
        return Main.menu_selected()
        
    def total_product_list():
        products = Product.product_list
        for i in range(len(products)):
            print(products[i][0], " " * 15,  products[i][2], " ", products[i][1])
            Calculator.total_price_foreign =+ products[i][1]
        print("")
        print("Total in foreign currency:", products[0][2] , " ", Calculator.total_price_foreign)
        print("")
    
    def tax_calculate():
        Calculator.duty = round(Calculator.total_price_THB * Calculator.duty_rate, 2)
#        duty_price = Calculator.total_price_THB + duty
        Calculator.vat = round((Calculator.total_price_THB + Calculator.duty) * 0.07, 2)
        
          
        
   
    
class Main:
    def user_login():
        for i in range(3):
            i = 2 - i
            print("Please Log-In with your registered account.")
            user_input = str(input("Username :"))
            password_input = str(input("Password :"))
            if user_input == UserData.id and password_input == UserData.password:
                print("Login Success : )")
                print("")
                return Main.menu_selected()
            else: 
                if i > 0:
                    print("Incorrect username or password. You can retry in", i, "Times")
                    print("")
                else : 
                    print("Please try again later : (")
                    quit()
            
    
    def print_welcome():
        print("Duty Calculator".center(40, "-"))
        print("_"*40)
        return Main.user_login()
        
    def menu_selected():
        print("Main Menu")        
        print("1.View today exchange rate")
        print("2.Duty calculator")
        print("3.Exit Program")
        print("")
        menu_input = input(str("Please select the menu number : "))
        print("")
        if menu_input == "1":
           return ExchangeRate.exchange_rate_list()
        elif menu_input == "2":
            return Product.add_product_quantity()
        elif menu_input == "3":
            return Main.exit_program()
        else:
            print("No menu selected. Please try again!!!")
            print("")
            return Main.menu_selected()
        
        
    def exit_program():
       print("Thank you".center(40, "_"))
       quit()        
        
        
        
Main.print_welcome()    
