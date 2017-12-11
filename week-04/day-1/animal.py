# Create Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one


class Animal:
    hunger = 50
    thirst = 50

    def eat(self):
        print("Omnomnomm")
        self.hunger -= 1

    def drink(self):
        print("gluck-gluck-gluuukkk")
        self.thirst -= 1
    
    def play(self):
        print("So much fun!")
        self.hunger += 1
        self.thirst += 1

    def checkstatus(self):
        print(" My hunger status is: " + str(self.hunger) + " \n My thirst status is: " + str(self.thirst))

tiger = Animal()
lion = Animal()
cougar = Animal()

tiger.play()
tiger.checkstatus()

lion.drink()
lion.checkstatus()