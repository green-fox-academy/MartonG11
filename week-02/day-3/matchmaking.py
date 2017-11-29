# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

order = [list(a) for a in zip(girls, boys)]

print(order)

# I don't think this is the perfect solution, but I have no idea how to solve it properly :(