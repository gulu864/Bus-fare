class Vehicle:

    def __init__(self):
        print("The Bus is here")
    def Fare(self):
        print("The Bus fare begins!")

class Bus(Vehicle):

    def __init__(self):

        super().__init__()
        super().Fare()

var1 = Bus()