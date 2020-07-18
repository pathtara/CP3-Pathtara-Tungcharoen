def login():
      for chance in range(3):
            chance = 2 - chance
            usernameInput = input("Username : ")
            passwordInput = input("Password : ")
            if usernameInput == "admin" and passwordInput == "1234":
                  print("Login Success")
                  print(showMenu())
                  choice = selectMenu()
                  if choice == 1:
                        price = float(input("Product price : "))
                        print("VAT = ", vatCalculate(price) - price) 
                  elif choice == 2:
                        print("Price : ", priceCalculate())                  
                  elif choice == 3:
                        print("Net price : ", netPriceCalculate())                                          
                  break
            else:
                  print("Incorrect username or password")
                  print("You can try within", chance, "times")
            if chance == 0:                  
                  print("Please try again later")            
def showMenu():
      print("----- iShop -----")
      print("1. Vat Calculator")
      print("2. Price Calculator")
      print("3. Net Price Calculator")
def selectMenu():
      userSelected = int(input(">>"))
      return userSelected
def priceCalculate():
      price1 = int(input("First Product Price : "))
      price2 = int(input("Second Product Price : "))
      return price1 + price2      
def vatCalculate(totalPrice):
      vat = 7
      result = totalPrice + (totalPrice * vat / 100)
      return result
def netPriceCalculate():
      price1 = int(input("First Product Price : "))
      price2 = int(input("Second Product Price : "))
      return vatCalculate(price1 + price2)      
      
print(login())
