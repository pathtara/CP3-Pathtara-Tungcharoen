print("Welcome to Pkung Cafe'")
print("<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
print(" ")
print("Please login your account to visit our store.")
print(" ")
########### account list ############
id = "pathtara"
password = "1234"
#####################################
idInput = input("Username : ")
passInput = input("Password : ")
if idInput == id and passInput == password:
      print("Login Success")
      print("")
      print("Welcome to Pkung Cafe'")
      print("")
      print("Beverage Menu")
      print("")
      print("americano  THB  80")
      print("latte      THB 120")
      print("moccha     THB 130")
      print("water      THB  15")
      print("______________________________") 
      print("")
      print("What would you like? : ")
      order1 = input("Menu name : ")
      no1 = int(input("No. of items : "))
      choice1 = input("Do you want anything else? (yes/no) : ")
      if choice1 == "yes":
            order2 = input("Menu name : ")           
            no2 = int(input("No. of items : "))         
            choice2 = input("Do you want anything else? (yes/no) : ")            
            if choice2 == "yes":
                  order3 = input("Menu name : ")
                  no3 = int(input("No. of items : "))              
                  choice3 = input("Do you want anything else? (yes/no) : ")               
                  if choice3 == "yes":
                        order4 = input("Menu name : ")
                        no4 = int(input("No. of items : "))                    
      if choice1 == "no":
            order2 = 0
            no2 = 0
            choice2 = "no"
      if choice2 == "no":
            order3 = 0
            no3 = 0
            choice3 = "no"
      if choice3 == "no":
            order4 = 0
            no4 = 0          
      if order1 == "americano" :
            price1 = 80
      elif order1 == "latte" :
            price1 = 120
      elif order1 == "moccha" :
            price1 = 130
      elif order1 == "water" :
            price1 = 15                     
      if order2 == "americano" :
            price2 = 80
      elif order2 == "latte" :
            price2 = 120
      elif order2 == "moccha" :
            price2 = 130
      elif order2 == "water" :
            price2 = 15
      elif order2 == 0 :
            price2 = 0      
      if order3 == "americano" :
            price3 = 80
      elif order3 == "latte" :
            price3 = 120
      elif order3 == "moccha" :
            price3 = 130
      elif order3 == "water" :
            price3 = 15
      elif order3 == 0 :
            price3 = 0                            
      if order4 == "americano" :
            price4 = 80
      elif order4 == "latte" :
            price4 = 120
      elif order4 == "moccha" :
            price4 = 130
      elif order4 == "water" :
            price4 = 15    
      elif order4 == 0 :
            price4 = 0                                                                                                              
      print("______________________________") 
      print("")
      print("Your Total price ") 
      print("")
      print("1.", order1, "___Qty", no1, "items___", "THB", price1,)
      if choice1 == "yes" :
            print("2.", order2, "___Qty", no2, "items___", "THB", price2,)
            if choice2 =="yes" :
                  print("3.", order3, "___Qty", no3, "items___", "THB", price3,)
                  if choice3 =="yes" :
                        print("4.", order4, "___Qty", no4, "items___", "THB", price4,)      
      net = price1 * no1 + price2 * no2 + price3 * no3 + price4 * no4
      vat = net * 0.07      
      print("")
      print("Total  THB", net)
      print("VAT (7%)   THB", vat)      
      print("______________________________") 
      print("Thank you")                
      print("Pkung Cafe'")                                                                         
else: 
      print("Incorrect username or password")
      print("Please try again.")