# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

shop_items = ["Cupcake", 2, "Brownie", False]

def changer(items):
    for n,i in enumerate(items):
        if i == 2:
            items[n] = "Croissant"
        elif i == False:
            items[n] = "Ice Cream"
    return(items)

print(changer(shop_items))

