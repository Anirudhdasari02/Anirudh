
class Plane:
    def __init__(self,wings,fly):
        self.wings = wings
        self.fly = fly
    def display(self):
        print(self.wings, self.fly)

class Jet(Plane):
    def __init__(self,wings,fly,color):
        Plane.__init__(self,wings,fly)
        self.color = color
    def display(self):
        print("no of wings:",self.wings)
        print("fly:",self.fly)
        print("color:",self.color)

class Passenger(Plane):
    def __init__(self,wings,fly,color):
        Plane.__init__(self,wings,fly)
        self.color = color
    def display(self):
        print("no of wings:",self.wings)
        print("fly:",self.fly)
        print("color:",self.color)      

obj1 = Jet("2", "yes","black")
obj2 = Jet("2", "yes", "white")
obj1.display()
obj2.display()

obj1 = Passenger("2", "yes","black")
obj2 = Passenger("2", "yes", "white")
obj1.display()
obj2.display()





 





        