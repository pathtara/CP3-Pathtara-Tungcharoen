
import firebase_admin
import numpy as np
from firebase_admin import credentials
from firebase_admin import db
from forex_python.converter import CurrencyRates as c
from columnar import columnar


# Connect to Firebase
cred = credentials.Certificate(
    'python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json'
    )
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://python3-born2dev.firebaseio.com/'
    })           
    
 
###################### Column format #########################
#header = ['No.', 'Name']
#data = [
#    [1, 'cat'],
#    [2, 'dog']
#]
#print(columnar(data, header, no_borders=True))
    
class StringFormat:
    result = ''
    
    def add_underline(string):
#        result = StringFormat.result
        result = ''
        for i in range(0, len(string)):
            if string[i] == ' ':
                result = result + string[i]
            else:
                result = result + string[i] + str('\u0332')
        return result
         

class MainWindow:
#    username = str()
    username = "admin"
    ref = db.reference('Users')
    
    def menu_select():
        selection = 0
        while True:
            try:
                selection = int(input("Menu selected No.: "))
                break
            except ValueError:
                print("Only number can be inputed. Please try again.")                
        return selection
        
    def welcome():
        shop_name = "Full Senses Phone&Gadget"
        header = [["Welcome to %s" % shop_name]]
        print(columnar(header, no_borders=False))
        print("1.Login")
        print("2.Register")
        selection = MainWindow.menu_select()
        if selection == 1:
            MainWindow.login()
        elif selection == 2:
            MainWindow.register()
        else:
            print("Invalid menu selected. Please try again.")
            MainWindow.welcome()
        
                
    def register():
        user_data = MainWindow.ref.get()
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
#        age = int(input("Age: "))  # Only number can be inputed
        ref = db.reference('Users')
        user_ref = ref.child(user_input)
        user_ref.set({
            'Password': password_input_1,
            'Firstname': first_name,
            'Lastname': last_name,
#            'age': age,
            'Authentication':'User'
            })                                                
        print("Register Complete.")
        MainWindow.welcome()
        
                    
    def login():
        ref = db.reference('Users')
        authentication = db.reference('Users/%s/Authentication' % MainWindow.username)
        user_data = ref.get()
        for i in range(0, 5):
            MainWindow.username = str(input("Username : "))
            password = str(input("Password : "))
            try:
                if MainWindow.username in (user_data.keys()) and password == str(user_data[MainWindow.username]['Password']):
                    print("Login Success")
                    if authentication.get() == "Admin":
                        MainWindow.main_menu_admin()
                        break
                    else:
                        MainWindow.main_menu()
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
                                        
    def main_menu_admin():
        header = [["Administrator Control"]]
        print(columnar(header,no_borders=False))
        print("1.Outstanding Product")
        print("2.Add Product")
        print("3.Delete Product")
        print("4.Exit Program")
        selection = 0
        try:
            selection = int(input("Menu Selected No.: "))
            if selection == 1:
                Products.outstanding_product()
                MainWindow.main_menu_admin()
            elif selection == 2:
                Products.add()
                MainWindow.main_menu_admin()
            elif selection == 3:
                Products.delete_code()
            elif selection == 4:
                MainWindow.exit_program()
            else:
                print("Invalid selection. Please try again")
        except ValueError:
            print("Only number can be inputed. Please try again.")    
            MainWindow.main_menu_admin()        
    
    
    def main_menu():
        print("1.Products List")
        print("2.Order Product")
        print("3.Show my cart")
        print("4.Exit Program")
        selection = 0
        try:
            selection = int(input("Menu Selected No.: "))
            if selection == 1 :
                print("Product List".center(30, "-"))
                Products.product_list()
                MainWindow.main_menu()
            elif selection == 2:
                print("Ordering".center(30, "-"))
                Cart.add_cart()
            elif selection == 3:
                Cart.cart_status()
            elif selection == 4:
                MainWindow.exit_program()
            else:
                print("No Menu Selected. Please try again.")
                MainWindow.main_menu()
        except ValueError:
            print("Only number can be inputed. Please try again.(Menu)")
#            return MainWindow.main_menu()                         


    def exit_program():
        print("Thank you".center(40, "-"))    
        SystemExit()


class MainVar:
    # ['Variable name', 'Description']
    product_var = [
        ['Category', 'Product Category'],
        ['Code', 'Product Code'],
        ['Name', 'Product Name'],
        ['Brand', 'Product Brand'],
        ['UnitPrice', 'Unit Price'],
        ['Quantity', 'Quantity']    
    ]
    
    
class Products:
    ref = db.reference('Products')        
    product_code = list()
    category = str()
    code = str()
    name = str()
    brand = str()
    unit_price = float()
    stock = int()
    
#    def product_code():
#        all_products = db.reference('Products')
#        product_code = list(all_products.get().keys())
#        return product_code

    def outstanding_product():
        ref = Products.ref
        product_code = Products.product_code
        dict = ref.get()
        categories = list(ref.get().keys())
        product_details = list()
        product_header = [ # ตั้งให้ auto gen
            'Code',
#            'Catagory',
            'Name',
#            'Brand',
#            'Unit Price',
            'Quantity'
        ]            
                
#         add code to list
        for i in range(len(categories)):
            products = list(ref.child(categories[i]).get().keys())
            for j in range(len(products)):
                Products.product_code.append(products[j])
                product_details.append([
                    products[j], 
#                    categories[i],
                    dict[categories[i]][products[j]]['Name'],
#                    dict[categories[i]][products[j]]['Brand'],
#                    dict[categories[i]][products[j]]['UnitPrice'],
                    dict[categories[i]][products[j]]['Quantity']
                ])
        print(StringFormat.add_underline('Outstanding Products'))
        print(columnar(product_details, product_header, no_borders=False))
        print("")
        
    def add(): # for admin use
        Products.outstanding_product()
        ref = Products.ref
        product_code = Products.product_code
        print("")
        print(product_code)
        # input product's category
        category_input = str(input("Product Category: "))
        # input product's code
        while True:
            code_input = str(input("Product Code: "))
            if code_input in product_code:
                print('This code has been registered')
                print('Please try again or type "exit" to return to menu')
            elif code_input.lower() == 'exit':
                print("")
                MainWindow.main_menu()
            else:
                break
        # input product's name
        name_input = str(input("Product Name: "))
        # input product's brand
        brand_input = str(input("Brand: "))
        # input unit price
        while True:
            try:
                unit_price_input = float(input("Unit Price: "))
                break
            except ValueError:
                print('Invalid amount. Please try again.')
        # input product's quantity
        while True:
            try:
                quantity_input = int(input("Quantity: "))
                break
            except ValueError:
                print('Invalid quantity. Please try again.')
        # print part
        product_added = ref.child('%s/%s' % (category_input, code_input))
        product_added.set({
        'Name':name_input,
        'Brand':brand_input,
        'UnitPrice':unit_price_input,
        'Quantity':quantity_input
        })
         
    def update():
        pass
        
    def delete_category():
        pass 
                       
    def delete_code():
        product_ref = Products.ref
        Products.outstanding_product()
        while True:
            delete_target = str(input('Input the product code you want to delete or type "exit" to return to main menu: ')).lower()
            category_key = list(product_ref.get().keys())
            for product_code in category_key:
                category_ref = product_ref.child(product_code)
                product_code = list(category_ref.get().keys())
                if delete_target in product_code:
                    print(delete_target)
                    product_ref.child('%s/%s' % (product_code, delete_target)).delete()
                    Products.outstanding_product()
                    print('Product code no.%s has been deleted.' % delete_target)
                    break
                elif delete_target.lower() == 'exit':
                    print("")
                    MainWindow.main_menu()
                else:
                    print('Invalid product code. Please try again.')
                print("")
                         
             
    def product_category():
        ref = Products.ref
        category = ref.get().keys()
        print(category)

        
    def product_list():
        ref = Products.ref
        category = list(ref.get().keys())
        header = [" ", "Product Name", "Product Price"]
        product_data = list()
        number = 0
        
        for i in range(len(category)):
            code = list(ref.child(category[i]).get().keys())
            product_category = category[i]
            for j in range(len(code)):
                number += 1
                name = db.reference('Products/%s/%s/Name' % (category[i],code[j])).get()
                price = round((db.reference('Products/%s/%s/UnitPrice' % (category[i], code[j])).get()), 2)
#                stock = db.reference('Products/%s/%s/Quantity' % (category[i], code[j])).get()
#                print("%d.%s      Price: %f    Stock: %d" % (number, name, price, stock))
                product_data.append([
                    [number],
                    [name],
                    [price],
#                    [stock] 
                ])
        print(columnar(product_data, header, no_borders=False))
        print("Shiping fee is equal USD 40.00 per shipment.")
        print("All price are subject to VAT 7%")
        print("Due to Thailand Custom Policy, import tax will not be charged for mobile phone.")
            
            
class Cart:
    
    cart = list()               
#    selected_code = str()
    selected_code = str()
    selected_qty = 0
    ref = db.reference('Carts')
    
    def create_cart():
        ref = db.reference('Carts')
        product = db.reference('Products').get()
        product_code = list(product)
        del product_code[0]
        print(product_code)
        print("")
        
        product_name = list(product['ip8_64'])
        print(product_name)
        print("")
        
        print(product['ip8_64']['Name'])
#        for i in product_code:
            
        my_cart = ref.child('%s' % MainWindow.username)
        my_cart.set({
        'Product':'test',
        'Price':0,
        'Quanty':0
        })
        
        print(my_cart.get())
    
    def list_cart():
        Cart.code_select()
        Cart.qty_select()      

    def listToDict():
        pass
        
        
    def add_cart():
#        Products.product_list()
        ref = Cart.ref
        print("")
        while True:
            Cart.code_select()
            Cart.qty_select() 
            Cart.check_cart()
                 
                           
            my_cart = ref.child(
            '%s/%s' % (MainWindow.username, Cart.selected_code)
            )
            add_product = my_cart.set({
            "code": Cart.selected_code,
            "quantity": Cart.selected_qty
            })
            print("Your products has been added to cart.")
            # add update cart details
            print("")
            
            
            
            print(ref_cart.get())
            print("")
            see_cart = ref_cart.child('%s' % MainWindow.username)
            rrr = db.reference('Carts')
            print(see_cart.get().keys())
            print("")

            
            
            
            choice = str(input("Do you want to continue order products? (Y/N): "))
            # ถ้ามีสินค้าอยู่แล้วให้ตั้งเป็น update
            if choice.upper() == "Y":
                True
            elif choice.upper() == "N":
                break
            else:
                print("(Please type (Y) or (N)")
                
    def check_cart(ref):
        cart_list = ref.child('%s' % MainWindow.username).get().keys()
#        cart_list.get().keys()
        print(cart_list)
        
    def update_cart():
        pass              
          
    def code_select():
        
        Cart.selected_code = str(input("Products Code: "))
        try:
            if Cart.selected_code in Products.product_code():
                return Cart.selected_code
            else:
                print("No product code found. Please try again.")
                return code_select()
        except NameError:
            print("Product selected not found. Please try again.")
            return Cart.code_select()                
            
    def qty_select():
            try:
                Cart.selected_qty = int(float(input("Quantity: ")))
            except TimeoutError:
                print("Only Number can be input. Please try again.(qty_select)")
                return Cart.qty_select()
                
    def cart_status():
        cart = db.reference('Carts/%s/code' % MainWindow.username)
#        cart_key = list(cart.get().keys())
#        print(cart_key['code'])
        print(cart.get())
        
        
############## Running Process ##############
#MainWindow.welcome()
Products.delete_code()

#Products.outstanding_product()
#ref = db.reference('Products')
#key = list(ref.get().keys())
#print(key)
#for i in key:
#    ref2 = ref.child(i)
#    key2 = list(ref2.get().keys())
#    print(key2)
#    forj in key
