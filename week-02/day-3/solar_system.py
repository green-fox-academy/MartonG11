# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]

def add_planet(solar):
    solar.insert(5, "Saturn")
    print(solar)

add_planet(planet_list)