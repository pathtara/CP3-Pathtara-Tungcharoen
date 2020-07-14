menuList = []
priceList =[]

def selectMenu():
    while True:
        menu = input("Please enter your menu : ")
        if menu.lower() == "done":
            break
        else: 
            menuPrice = float(input("Please enter price : "))
            menuList.append(menu)
            priceList.append(menuPrice)        
        
        
def totalPrice():
    total = sum(priceList)
    return round(total, 2)
   
   
def vatCal(totalPrice):
   vat = (totalPrice) * 0.07
   return round(vat, 2)
   
   
def netPrice(totalPrice):
    net = totalPrice() + vatCal(totalPrice())
    return round(net,2 )   

def showBill():
    print("My Orders".center(20, "-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])        
    print("")
    print("Total Price : ", totalPrice(), " THB")
    print("VAT 7% : ", vatCal(totalPrice()), " THB")
    print("Net Price : ", netPrice(totalPrice), "THB")
    print("-" * 20)
    print("Thank you".center(20, "-"))
    

print("Welcome to myCafe'".center(20, "-"))       
selectMenu()
print("")
showBill()
