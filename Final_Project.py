
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from forex_python.converter import CurrencyRates as c


class FireBase:
    def firebase_login():
#        cred = credentials.Certificate(
#            'python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json'
#            )
        cred = credentials.Certificate(
            'python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json'
            )
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://python3-born2dev.firebaseio.com/'
            })
        

class MainWindow:
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
                                        

    def main_menu():
        print("1.Products List")
        print("2.Order Product")
        print("3.Our Profile")
        print("4.Exit Program")
        selection = 0
        try:
            selection = int(input("Menu Selected: "))
            if selection == 1 :
                pass
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                return MainWindow.exit_program()
            else:
                print("No Menu Selected. Please try again.")
                return MainWindow.main_menu()
        except:
            print("Only number can be inputed. Please try again.")
            return MainWindow.main_menu()                         


    def exit_program():
        print("Thank you".center(40, "-"))    
        SystemExit()



class Products:
        
    def product_list():
        all_products = db.reference('Products')
        print(all_products.get().keys())
        product_code = list(all_products.get().keys())
        for i in range(len(product_code)):
            number = i+1
            code = product_code[i]
            name = db.reference('Products/%s/Name' % code)
            price = db.reference('Products/%s/Price' % code)
            stock = db.reference('Products/%s/Stock' % code)
            print("%d.%s      Price: %d    Stock: %d" % (number, name.get(), price.get(), stock.get()))
        print("Shiping fee is equal USD 40.00 per shipment.")
        print("All price are subject to VAT 7%")
        print("Due to Thailand Custom Policy, import tax will not be charged for mobile phone.")
            
            
class Cart:
    cart = list()               
    selected_code = ""
    selected_qty = 0
    
    def add_cart():
        Products.product_list()
        print("")
        while True:
            Cart.code_select()
            Cart.qty_select()      
            add_code = db.reference('Product').get()
            
    def code_select():
        Cart.selected_code = str(input("Products Code: "))
        if selected_code in Products.product_code:
            pass
        else:
            print("No product code found. Please try again.")
            return Cart.code_select()
            
    def qty_select():
            try:
                Cart.selected_qty = int(input("Quantity: "))
            except:
                print("Only Number can be input. Please try again.")
                return Cart.qty_select()
                    
        
        
#FireBase.firebase_login()
#Products.product_list()
#MainWindow.register()
#MainWindow.login()

#Cart.add_cart()
