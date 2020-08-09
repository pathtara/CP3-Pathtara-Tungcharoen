
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from forex_python.converter import CurrencyRates as c


class FireBase:
    def firebase_login():
        cred = credentials.Certificate(
            'python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json'
            )
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://python3-born2dev.firebaseio.com/'
            })
            

class MainWindow:
    
    username = str()
    
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
            MainWindow.username = str(input("Username : "))
            password = str(input("Password : "))
            try:
                if MainWindow.username in (user_data.keys()) and password == str(user_data[MainWindow.username]['password']):
                    print("Login Success")
                    return MainWindow.main_menu()
                    break
                else:
                    pass
            except KeyError:
                pass
            print("Incorrect username or password. Please try again.")
            print("You can try in %d times" % (4 - i))
            print("")
        MainWindow.exit_program()
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
                print("Product List".center(30, "-"))
                Products.product_list()
                MainWindow.main_menu()
            elif selection == 2:
                print("Ordering".center(30, "-"))
                Cart.add_cart()
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
    
    def product_code():
        all_products = db.reference('Products')
        product_code = list(all_products.get().keys())
        return product_code
        
    def product_list():
        all_products = db.reference('Products')
        product_code = list(all_products.get().keys())
        for i in range(len(Products.product_code())):
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
    selected_code = str()
    selected_qty = 0
    
    def add_cart():
        Products.product_list()
        print("")
        while True:
            Cart.code_select()
            Cart.qty_select()      
            system_products = db.reference('Products')
            my_cart = db.reference('Carts/%s' % MainWindow.username)
            add_price = my_cart.push({
            "code": Cart.selected_code,
            "quantity": Cart.selected_qty
            })
            print("Your products has been added to cart.")
            # add update cart details
            print("")
            print(add_price.get())
            choice = str(input("Do you want to continue order products? (Y/N): "))
            # ถ้ามีสินค้าอยู่แล้วให้ตั้งเป็น update
            if choice.upper() == "Y":
                True
            elif choice.upper() == "N":
                break
            else:
                print("(Please type (Y) or (N)")
          
    def code_select():
        Cart.selected_code = str(input("Products Code: "))
        if Cart.selected_code in Products.product_code():
            return Cart.selected_code
        else:
            print("No product code found. Please try again.")
            return code_select()
            
    def qty_select():
            try:
                Cart.selected_qty = int(input("Quantity: "))
            except:
                print("Only Number can be input. Please try again.")
                return Cart.qty_select()
                

FireBase.firebase_login()
MainWindow.login()
#Cart.add_cart()
#print("ppp",Cart.selected_code)
print(MainWindow.username)
