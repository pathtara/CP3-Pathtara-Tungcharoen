menuList = []
def createBill():
    totalPrice = 0
    print("")
    print("Order List".center(20, "-"))
    for i in range(len(menuList)):
        print("%s      %d THB" % (menuList[i][0], menuList[i][1]))
        totalPrice += menuList[i][1]
    print("Total Price :  %d THB" % totalPrice)   


def start():                            
    while True:
        menu = input("Please fill your orders : ")
        if menu.lower() == "done" :
            break
        else:
            price = int(input("Please fill the price : "))
            menuList.append([menu, price])
start()            
createBill()        
