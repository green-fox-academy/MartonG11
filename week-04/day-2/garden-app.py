class Flower():
    water_amount = 0


    def __init__(self,name):
        self.name = name

    def water_checker(self):
        self.water_amount = water_amount
        if water_amount <= 5:
            print(self.name + " needs water!")
        else:
            pass

virag = Flower("virag")
virag.water_checker()
