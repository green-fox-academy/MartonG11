# Create SantaFactory and help Santa bring the remaining toys to the poor children.
# There are 3 kind of toys:
# - Doll, it costs 25, and can be different colour.
# - Dotted ball, costs 10, and can be different colour and size.
# - Jumping rope, costs 15, and can be different length.
# Each toy have an owner, when produced the owner should be nil.
# The starting balance of the factory is 200.
# It can produce toys until the balance is higher than 0.
# Create the produce method.
# The produced toys are going into Santa's bag as you can see below in the example.
# Santa brings the toys to the children until there is something in the bag.
# When a toy is being delivered, it gets it's owner (a random children name) and gets removed from the bag.
# Create the bring method.

import random

children = ["Peter", "Lily", "John", "Jane"]

class SantaFactory(object):
    def __init__(self,balance=200):
        self.balance = balance

    def produce(self, name="", colour=0, size=0, length=0):
        toy = None
        if name == "doll":
            
            if self.balance >= 25:
                toy = Doll(colour)
                self.balance -= 25
        if name == "ball":
            
            if self.balance >= 10:
                toy = Ball(colour,size)
                self.balance -= 10
        if name == "rope":
            
            if self.balance >= 15:
                toy = Rope(length)
                self.balance -= 15
        return toy

    def get_balance(self):
        return str(self.balance)


class SantaBag(object):
    def __init__(self, produced_toys=[]):
        self.produced_toys = produced_toys
    
    def add(self,produce):
        self.produced_toys.append(produce)

    def get_number_of_items(self):
        return len(self.produced_toys)

    def bring_toys_to_children(self):
        for toy in range(len(self.produced_toys)):
            child = random.choice(children)
            self.produced_toys[toy].owner = child
            self.produced_toys.remove(toy)




class Toy(object):
    def __init__(self,owner,cost):
        self.owner = owner
        self.cost = cost

class Doll(Toy):
    def __init__(self,colour):
        super().__init__(0,25)
        self.colour = colour

class Ball(Toy):
    def __init__(self,colour,size):
        super().__init__(0,10)
        self.colour = colour
        self.size = size

class Rope(Toy):
    def __init__(self,length):
        super().__init__(0,15)
        self.length = length











santa_bag = SantaBag()
santa_factory = SantaFactory()
santa_bag.add(santa_factory.produce('doll', 'pink'))
santa_bag.add(santa_factory.produce('ball', 'blue', 3))
santa_bag.add(santa_factory.produce('ball', 'yellow', 1))
santa_bag.add(santa_factory.produce('rope', 22))
# The output should be 'The factory's balance is: 140'
print('The factory\'s balance is: ' + santa_factory.get_balance())
# The output should be 'There are 4 undelivered toys in Santa's bag.'
print('There are {} toys in Santa\'s bag.'.format(santa_bag.get_number_of_items()))
santa_bag.bring_toys_to_children() # itt nem metódusként volt meghívva
# The output should be 'There are 0 undelivered toys in Santa's bag.'
print('There are {} toys in Santa\'s bag.'.format(santa_bag.get_number_of_items()))