import firebase_admin
import numpy as np
from firebase_admin import credentials
from firebase_admin import db
from forex_python.converter import CurrencyRates as c
from columnar import columnar


# Connect to Firebase
cred = credentials.Certificate(
    "python3-born2dev-firebase-adminsdk-lvxno-853811d7e7.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://python3-born2dev.firebaseio.com/"}
)


class StringFormat:
    result = ""

    def add_underline(string):
        #        result = StringFormat.result
        result = ""
        for i in range(0, len(string)):
            if string[i] == " ":
                result = result + string[i]
            else:
                result = result + string[i] + str("\u0332")
        return result


class MainWindow:
    username = str()
    ref = db.reference("Users")

    def menu_select():
        selection = 0
        while True:
            try:
                selection = int(input("Menu selected No.: "))
                print("")
                break
            except ValueError:
                print("Only number can be inputed. Please try again.")
                print("")
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
            print("")
            MainWindow.welcome()

    def register():
        user_data = MainWindow.ref.get()
        while True:
            user_input = str(input("Username: "))
            if user_input in user_data.keys():
                print("Username alreadys exists, please try the different one.")
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
        ref = db.reference("Users")
        user_ref = ref.child(user_input)
        user_ref.set(
            {
                "Password": password_input_1,
                "Firstname": first_name,
                "Lastname": last_name,
                #            'age': age,
                "Authentication": "User",
            }
        )
        print("Register Complete.")
        print("Returning to mainmenu")
        print("")
        MainWindow.welcome()

    def login():
        ref = db.reference("Users")
        user_data = ref.get()
        for i in range(0, 5):
            MainWindow.username = str(input("Username : "))
            password = str(input("Password : "))
            authentication = db.reference(
                "Users/%s/Authentication" % MainWindow.username
            )
            try:
                if MainWindow.username in (user_data.keys()) and password == str(
                    user_data[MainWindow.username]["Password"]
                ):
                    print("Login Success")
                    print("")
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
        MainWindow.welcome()
        # back to main menu

    def main_menu_admin():
        header = [["Administrator Control"]]
        print(columnar(header, terminal_width=100, min_column_width=50, justify="c"))
        print("1.Outstanding Product")
        print("2.Add Product")
        print("3.Delete Product")
        print("4.Exit Program")
        selection = 0
        try:
            selection = int(input("Menu Selected No.: "))
            if selection == 1:
                print("")
                Products.outstanding_product()
                MainWindow.main_menu_admin()
            elif selection == 2:
                print("")
                Products.add()
                MainWindow.main_menu_admin()
            elif selection == 3:
                print("")
                Products.delete_code()
            elif selection == 4:
                print("")
                pass
            else:
                print("Invalid selection. Please try again")
                print("")
        except KeyError:
            print("Only number can be inputed. Please try again.")
            print("")
            MainWindow.main_menu_admin()

    def main_menu():
        header = [["Main Menu"]]
        print(columnar(header, terminal_width=100, min_column_width=50, justify="c"))
        print("1.Products List")
        print("2.Order Product")
        print("3.Show my cart")
        print("4.Check out my order")
        print("5.Exit Program")
        selection = 0
        try:
            selection = int(input("Menu Selected No.: "))
            if selection == 1:
                print("")
                print("Product List".center(30, "-"))
                Products.product_list()
                MainWindow.main_menu()
            elif selection == 2:
                print("")
                print("Ordering".center(30, "-"))
                Cart.add_cart()
            elif selection == 3:
                print("")
                Cart.show_my_cart()
            elif selection == 4:
                print("")
                Cart.check_out()
            elif selection == 5:
                print("")
                MainWindow.exit_program()
            else:
                print("No Menu Selected. Please try again.")
                print("")
                MainWindow.main_menu()
        except ValueError:
            print("Only number can be inputed. Please try again.")
            print("")
            MainWindow.main_menu()

    def exit_program():
        print("Thank you".center(50, "-"))
        print("")
        MainWindow.username = ""
        MainWindow.welcome()


class MainVar:
    # ['Variable name', 'Description']
    product_var = [
        ["Category", "Product Category"],
        ["Code", "Product Code"],
        ["Name", "Product Name"],
        ["Brand", "Product Brand"],
        ["UnitPrice", "Unit Price"],
        ["Quantity", "Quantity"],
    ]


class Products:
    ref = db.reference("Products")
    product_code = []
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
        product_code = list(ref.get().keys())
        product_details = list()
        table_name = [["Products"]]
        product_header = [  # ตั้งให้ auto gen
            "Code",
            "Catagory",
            "Name",
            "Brand",
            "Unit Price",
            "Quantity",
        ]
        for code in product_code:
            dict = ref.child(code).get()
            #            dict = ref.order_by_child('%s/Category' % code).get()
            product_details.append(
                [
                    code,
                    dict["Category"],
                    dict["Name"],
                    dict["Brand"],
                    dict["UnitPrice"],
                    dict["Quantity"],
                ]
            )
        product_details.sort(key=len)
        # ทำsort by catagory/code
        print(columnar(table_name))
        print(
            columnar(product_details, product_header, terminal_width=100, justify="c")
        )

    def add():  # for admin use
        Products.outstanding_product()
        ref = Products.ref
        product_code = Products.product_code
        print("")
        category_input = str(input("Product Category: "))
        while True:
            code_input = str(input("Product Code: "))
            if code_input in product_code:
                print("This code has been registered")
                print('Please try again or type "exit" to return to menu')
            elif code_input.lower() == "exit":
                print("")
                MainWindow.main_menu()
            else:
                break
        name_input = str(input("Product Name: "))
        brand_input = str(input("Brand: "))
        while True:
            try:
                unit_price_input = float(input("Unit Price: "))
                break
            except ValueError:
                print("Invalid amount. Please try again.")
        while True:
            try:
                quantity_input = int(input("Quantity: "))
                break
            except ValueError:
                print("Invalid quantity. Please try again.")
        product_added = ref.child(code_input)
        product_added.set(
            {
                "Category": category_input,
                "Name": name_input,
                "Brand": brand_input,
                "UnitPrice": unit_price_input,
                "Quantity": quantity_input,
            }
        )

    def update():
        pass

    def delete_category():
        pass

    def delete_code():
        product_ref = Products.ref
        Products.outstanding_product()
        product_code = list(product_ref.get().keys())
        while True:
            delete_target = str(
                input(
                    'Input the product code you want to delete or type "exit" to return to main menu: '
                )
            ).lower()
            stop = ""
            for i in product_code:
                if delete_target in product_code:
                    product_ref.child(delete_target).delete()
                    Products.outstanding_product()
                    print("Product code no.%s has been deleted." % delete_target)
                    stop = "Y"
                elif delete_target.lower() == "exit":
                    print("")
                    MainWindow.main_menu()
                    return False
                else:
                    stop = "N"
            if stop == "N":
                print("Invalid product code. Please try again.")
                print("")
            else:
                pass

    def product_category():
        ref = Products.ref
        category = ref.get().keys()
        print(category)

    def product_list():
        Products.outstanding_product()
        print("Shiping fee is equal USD 40.00 per shipment.")
        print("All price are subject to VAT 7%")
        print(
            "Due to Thailand Custom Policy, import tax will not be charged for mobile phone."
        )
        print("")
        
class Cart:
    cart = list()
    selected_code = str()
    selected_qty = 0
    cart_ref = db.reference("Carts/%s" % MainWindow.username)

    def list_cart():
        Cart.code_select()
        Cart.qty_select()

    def add_cart():
        cart_ref = Cart.cart_ref
        print("")
        Products.product_list()
        print("")
        while True:
            product_code = Cart.code_select()
            if product_code == "exit":
                MainWindow.main_menu()
                break
            else:
                selected_qty = Cart.qty_select(product_code)
                my_cart = db.reference("Carts/%s" % MainWindow.username)
                cart_qty = db.reference(
                    "Carts/%s/%s/Quantity" % (MainWindow.username, product_code)
                ).get()
                stock = db.reference("Products/%s" % product_code)
                stock_qty = db.reference(
                    "Products/%s/Quantity" % (product_code)
                ).get()
                my_cart.update({
                    product_code: {
                        "Quantity": (cart_qty + selected_qty)
                    }
                })
                stock.update({
                    "Quantity": (stock_qty - selected_qty)
                })
                Cart.show_my_cart()
                print("Your products has been added to cart.")
                print("")
                print(cart_ref.get())
                print("")
                print(my_cart.get().keys())
                print("")

    def show_my_cart():
        print("My Cart".center(30, "-"))
        my_cart = db.reference("Carts/%s" % MainWindow.username).get()
        product = db.reference("Products").get()
        my_products = list(my_cart.keys())
        cart_list = list()
        cart_header = ["Code", "Name", "Brand", "Price", "Quantity"]
        for code in my_products:
            cart_list.append(
                [
                    code,
                    product[code]["Name"],
                    product[code]["Brand"],
                    product[code]["UnitPrice"],
                    my_cart[code]["Quantity"],
                ]
            )
        print(columnar(cart_list, cart_header, terminal_width=100))
        print("")
        print("Cart's Menu".center(30, "-"))
        menu_selected = Cart.cart_menu_selected()
        MainWindow.main_menu()
        
    def cart_menu_selected():
        while True:
            pass
            
    
    def code_select():
        while True:
            print('Type the product code or type "exit" to return to main menu.')
            selected_code = str(input("Products Code: ")).lower()
            try:
                code = list(db.reference("Products").get().keys())
                if selected_code.lower() == "exit":
                    return selected_code
                    break
                elif selected_code in code:
                    return selected_code
                    break
                else:
                    print("No product code found. Please try again.")
                    print("")
            except NameError:
                print("Product selected not found. Please try again.")
                print("")

    def qty_select(product_code):
        while True:
            try:
                selected_qty = int(float(input("Quantity: ")))
                system_qty = int(
                    db.reference("Products/%s/Quantity" % product_code).get()
                )
                if selected_qty > system_qty:
                    print("Not enought quantity. Please try again.")
                    print("")
                else:
                    return selected_qty
                    break
            except ValueError:
                print("Only Number can be input. Please try again.")
                print("")

    def check_out():
        cart_ref = db.reference("Carts/%s" % MainWindow.username)
        product_ref = db.reference("Products")


############## Running Process ##############
MainWindow.welcome()
