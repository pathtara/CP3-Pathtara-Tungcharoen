class Customer:
    name = ""
    lastName = ""
    age = 0
    
    def addCart(self):
        print("Add product to", self.name, self.lastName, "'s Cart")
        
customer1 = Customer()
customer1.name = "Bank"
customer1.lastName = "B."
customer1.addCart()   

customer2 = Customer()
customer2.name = "Aum"
customer2.lastName = "T."
customer2.addCart()

customer3 = Customer()
customer3.name = "Pop"
customer3.lastName = "D."
customer3.addCart()

customer4 = Customer()
customer4.name = "Put"
customer4.lastName = "J."
customer4.addCart()