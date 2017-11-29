

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away


example = "In a dishwasher far far away"



def changer(name):
     new_name = name.replace("dishwasher", "galaxy")
     print(new_name)

changer(example)