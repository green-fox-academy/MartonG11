# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys

def favourite():
    if len(sys.argv) == 1:
        print(''' fav_animals [animal] [animal] ''')
    elif len(sys.argv) > 1 and sys.argv[1] == "fav_animals":
        input_animals = sys.argv[2:] #kettőtől megnézi az összes argumentumot a végéig
        favorites = set() #csinál egy üres halmazt, azért set, mert kiszedi az ismétlődéseket
        with open("favourites.txt",'r') as in_file:
            animals = in_file.readlines() #beolvasom a sorokat
            for animal in animals:
                favorites.add(animal.strip()) 
                # "       \n\n\n\n\t\t\thello      \t\t\n\n\n world\n\n\n    \t\t   ! \n\n".strip()
                # "hello      \t\t\n\n\n world\n\n\n    \t\t   !" végéről és elejéről leszedi
                
        for animal in input_animals:
            favorites.add(animal)
        with open("favourites.txt","w") as out_file:
            out_file.write("\n".join(favorites))
        
    else:
        print("usage: fav_animals")


favourite()