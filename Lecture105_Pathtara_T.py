class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on Air / code", self.licenseCode)
        
class Car(Vehicle):
    licenseCode = "1111"
    def talk(self):
        print("Hey Yo!!")
    
class PickUp(Vehicle):
    licenseCode = "2222"
    
class Van(Vehicle):
    licenseCode = "3333"
    
class EstateCar(Vehicle):
    licenseCode = "4444"
    
car1 = Car()
car1.turnOnAirConditioner()
car1.talk()            

pickup1 = PickUp()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()
                                                                                                                                                                                
        

