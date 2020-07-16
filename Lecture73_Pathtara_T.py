menuList = []
systemMenu = {"Coffee":120, 'Cake':45, "Water":15}

def createBill():
    totalPrice = 0
    print("")
    print("Order List".center(20, "-"))
    for i in range(len(menuList)):
        print("%s                    %d THB" % (menuList[i][0], menuList[i][1]))
        totalPrice += menuList[i][1]
    print("Total Price :  %d THB" % totalPrice)   

def menuName():
    print("Menu".center(30,"-"))
    for i in systemMenu :
        print("%s                    %d THB" % (i, systemMenu[i]))

def start():
    print("Welcome to myCafe")
    print("")
    menuName()
    while True:
        menu = input("Please select your orders : ")
        if menu.lower() == "done" :
            break
        else:
            menuList.append([menu, systemMenu[menu.capitalize()]])
            
        
start()            
createBill()      
