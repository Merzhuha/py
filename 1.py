class cars():
    def __init__(self, brand, cost):
        self.brand=brand
        self.cost=cost
    def sold(self):
        print("The car's brand is " + self.brand + " cost is " + str(self.cost)+'$')
car1=cars("Mustang", 1000000)
car2=input(cars())
car1.sold()