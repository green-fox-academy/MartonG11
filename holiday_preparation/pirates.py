import random

class Pirate(object):
    def __init__(self):
        self.drinks = 0
        self.dead = False
        self.passed_out = False
    
    def is_alive(self):
        return self.dead == False
    
    def is_conscious(self):
        return self.passed_out == False
    
    def can_drink(self):
        if not self.is_alive():
            print("he's dead.")
        return self.is_conscious()
    
    def drink_some_rum(self):
        if self.can_drink():
            self.drinks += 1
    
    def hows_it_going_mate(self):
        if self.can_drink():
            if self.drinks < 5 :
                print("Pour me anudder!")
            else:
                print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
                self.pass_out()
                
    def pass_out(self):        
        self.passed_out = True

    def die(self):
        self.pass_out()
        self.dead = True
    
    def brawl(self, other_pirate):
        if self.is_conscious():
            if other_pirate.is_conscious():
                chance = random.randint(1,3)
                if chance == 1:
                    other_pirate.die()
                elif chance == 2: 
                    self.die()
                else:
                    self.pass_out()
                    other_pirate.pass_out()
            else: 
                 other_pirate.die()
                
            
class Ship(object):


    def __init__(self):
        self.crew = list() # or []
        self.captain = None
        
    def fill_ship(self):
        self.captain = Pirate()
        crewnumber = random.randint(10,20)
        self.crew = [Pirate() for i in range(crewnumber)]
    
    def count_alive(self):
        alive_count = 0 
        for pirate in self.crew:
            alive_count += pirate.is_alive()
        return alive_count
    
    def __str__(self):
        drinks = 0
        state = "Not assigned"
        alive_count = self.count_alive()
        
        if self.captain is not None:
            drinks = self.captain.drinks
            if self.captain.is_alive():
                alive_count += 1
                if self.captain.is_conscious():
                    state = "Alive"
                else:
                    state = "Passed out"
            else:
                state = "Dead"
            
        
        
        return "\n".join(["Rum consumed by captain: {drinks}",
                          "State of captain: {state}",
                          "Crewmembers alive: {alive_count}"]).format(drinks=drinks, 
                                                                       state=state,
                                                                       alive_count=alive_count)
    
    def battle(self, other_ship):
        score = self.count_alive() - self.captain.drinks
        other_score = other_ship.count_alive() - other_ship.captain.drinks
        
        if score > other_score:
            winner = self
            loser = other_ship
        elif score < other_score:
            winner = other_ship
            loser = self
        else:
            return
            
        
        get_killed = random.randint(0,loser.count_alive())
        for pirate in loser.crew:
            if get_killed == 0:
                break
            if pirate.is_alive():
                pirate.die()
                get_killed -= 1
                
        rum_reward = random.randint(0,winner.count_alive())
        for pirate in winner.crew: 
            if rum_reward == 0:
                break
            if pirate.is_conscious():
                pirate.drink_some_rum()
                rum_reward -= 1
        winner.captain.drink_some_rum()
                