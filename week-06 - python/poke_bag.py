# Create a PokeBag class that can store multiple pokemons from different types. Add 5 pokemons to your PokeBag.
# There are 3 kind of pokemons:
# - Pikachu, who says “Pika-pika” and has 12 HP (health point)
# - Bulbasaur, who says “Bulba-saur” and has 10 HP
# - Charmander, who says “Char-char” and has 10 HP
# Every pokemon has a random strength between 1 and 10.
# Pokemons can say their sound (see above) when their Speak method is called. The Speak method should return the pokemon’s sound.
# Create a function that returns the pokemon with the highest strength. In case of equal strengths, it’s your choice which one to return.

# from operator import attrgetter
import random

class Pokemon(object):
    def __init__(self,sound,hp):
        self.sound = sound
        self.hp = hp
        self.strength = random.randint(1,10)
    
    def speak(self):
        return self.sound
    
    def get_strength(self):
        return self.strength
    
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(sound="Pika-pika",hp=12)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(sound="Bulba-saur",hp=10)
    
class Charmander(Pokemon):
    def __init__(self):
        super().__init__(sound="Char-char",hp=10)

class PokeBag(object):
    def __init__(self):
        self.pokemons = []

    def add(self,pokemon_type):
        self.pokemons.append(pokemon_type)

    def get_strongest(self):
        #self.pokemons.sort(key=attrgetter('strength'),reverse=True)
        self.pokemons.sort(key=Pokemon.get_strength,reverse=True)
        return self.pokemons[0]


    def get(self,number):
        return self.pokemons[number]

    def test_print(self):
        print([pokemon.strength for pokemon in self.pokemons])



# 
# Example:
pokeBag = PokeBag()
pokeBag.add(Pikachu())
pokeBag.add(Pikachu())
pokeBag.add(Pikachu())
pokeBag.add(Bulbasaur())
pokeBag.add(Charmander())

print(pokeBag.get(0).speak())

# This should print Pika-pika

strongestPokemon = pokeBag.get_strongest()

print(strongestPokemon.speak(),strongestPokemon.strength)
pokeBag.test_print()
# Should return the pokemon with the highest strength value