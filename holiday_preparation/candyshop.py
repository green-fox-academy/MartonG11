# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candy's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#

# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candy or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candy or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"


# "Inventory: 3 candies
# "Inventory: {candy_amount} candies

# Income: 100
# {Income} income
# Income: {income}


# Create a CandyShop class

class CandyShop(object):

    def __init__(self, sugar):
         self.sugar = sugar
         self.candies = 0
         self.lollipops = 0
         self.income = 0
         self.candy_price = 20
         self.lollipop_price = 10
         
    def create_sweets(self, sweet_name):
        if sweet_name == "candy":
            if self.sugar >= 10:
                 self.sugar -= 10
                 self.candies += 1 
        if sweet_name == "lollipop":
            if self.sugar >= 5:
                 self.sugar -= 5
                 self.lollipops += 1 
             
             
         
    def raise_prices(self, percentage):
        price_raise = 1 + percentage/100
        self.candy_price *= price_raise
        self.lollipop_price *= price_raise

             
    def sell(self, sweet_name, amount):
        if sweet_name == "candy":
            if 0 < amount <= self.candies:
                 self.candies -= amount
                 self.income += amount * self.candy_price
        if sweet_name == "lollipop":
             if 0 < amount <= self.lollipops:
                 self.lollipops -= amount
                 self.income += amount * self.lollipop_price
     
    def buy_sugar(self, amount):
        sugar_price = amount * 0.1
        if self.income >= sugar_price:
            self.income -= sugar_price
            self.sugar += amount
         
    def __str__(self):
        return "Inventory: {candy_amount} candies, {lollipop_amount} lollipops, Income: {income}, Sugar: {sugar}gr".format(
        candy_amount=self.candies,
        lollipop_amount=self.lollipops,
        income=self.income,
        sugar=self.sugar)
     
     
     
     


candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Inventory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Inventory: 1 candies, 2 lollipops, Income:20, Sugar: 270gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Inventory: 1 candies, 1 lollipops, Income:30.5, Sugar: 270gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Inventory: 1 candies, 1 lollipops, Income:5, Sugar: 570gr"


