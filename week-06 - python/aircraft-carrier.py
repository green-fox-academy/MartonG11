# BEFORE I START:
# Is a? -> inheritance
# Has a? -> membership
# Neither? -> seperate object

class Aircraft(object):
    def __init__(self, max_ammo,base_damage):
        self.base_damage = base_damage
        self.max_ammo = max_ammo
        self.ammo = 0
        
    def fight(self):
        damage_dealt = self.ammo * self.base_damage
        self.ammo = 0
        return damage_dealt
     
    def refill(self,ammonumber):
        ammo_needed = self.max_ammo - self.ammo
        ammo_available = min(self.max_ammo,max(0,ammonumber)) #max(0,) ---> kizárom a negatív lehetőségét, mert akkor 0-val tér vissza 
        ammo_to_fill = min(ammo_needed,ammo_available)
        self.ammo += ammo_to_fill 
        ammonumber -= ammo_to_fill
        return ammonumber
        
        
    def getType(self):
        return "Aircraft"
        
    def getStatus(self):
        return"Type {aircraft_type}, Ammo: {ammo}, Base Damage: {basedamage}, All Damage: {alldamage}".format(aircraft_type=self.getType(), ammo=self.ammo, basedamage=self.base_damage, alldamage = (self.ammo * self.base_damage))

class F16(Aircraft):
    def __init__(self):
        super().__init__(8,30)
    
    def getType(self):
        return("F16")

class F35(Aircraft):
    def __init__(self):
        super().__init__(12,50)
    
    def getType(self):
        return("F35")
    
class Carrier(object): 
    def __init__(self,ammo,healthpoint):
        self.stored_aircrafts = []
        self.healthpoint = healthpoint
        self.ammo = ammo
        
    def addAircraft(self,aircraft_type):
        if aircraft_type == "F16":
            self.stored_aircrafts.append(F16())
        if aircraft_type == "F35":
            self.stored_aircrafts.insert(0,F35()) #insert(0,F5()), because I want to place them before the F16s for the fill method
            
    def fill(self):
        if self.ammo == 0: 
            raise ValueError("The ammo is zero.") #throw exception
        for aircraft in self.stored_aircrafts:
            self.ammo = aircraft.refill(self.ammo)
            if self.ammo == 0:
                break


    def fight(self,other_carrier):
        total_damage = sum(aircraft.fight() for aircraft in self.stored_aircrafts)
        other_carrier.healthpoint - total_damage

    def getStatus(self):
        if self.healthpoint <= 0:
            return("It's dead Jim :(")
        else:
            return("HP: {Health}, Aircraft count: {number_of_aircrafts}, Ammo Storage: {total_ammo}, Total damage: {damagedealt}".format(Health=self.healthpoint, number_of_aircrafts=len(self.stored_aircrafts), damagedealt=self.fight()))



carrier = Carrier(80,1000)
carrier.addAircraft("F16")
carrier.addAircraft("F35")
carrier.addAircraft("F16")
carrier.addAircraft("F35")
carrier.addAircraft("F16")
carrier.fill()