class Vehicle:

    def __init__(self):
        print("The Bus is here")
    
    def Fare(self):
        print("The Bus fare begins!")
    def Seats(self):
        print("Bus number 1 has 10 seats.")
        print("Bus number 2 has 12 seats.")
        print("Bus number 3 has 16 seats.")

class Bus(Vehicle):

    def __init__(self):

        super().__init__()
        super().Fare()

var1 = Bus()