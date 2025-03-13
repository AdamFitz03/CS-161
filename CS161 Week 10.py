# Adam Fitzpatrick
# Week 10

import math

class SolarObject:
    """Solar object PArent class to hold and define the attributes for AU distance, spin and orbit time"""
    def __init__(self,distance_au,spin,orbit_average):
        self.distance_au=distance_au
        self.spin=spin
        self.orbit_average=orbit_average

    def colonization(self):
        """ Method to calculate life potential of solar objects based on distance AU, with earths
            population of 6 billion as the base population number. It then returns the value rounded to 2 decimal places."""
        life_potential = 6000000000/self.distance_au
        return round(life_potential,2)

    def spin(self):
        """ Does almost nothing, but it does take the spin method and passes it to the child classes"""
        pass

class Planets(SolarObject):
    """Inherits the attributes from the solar objects class and uses super inheritance and polymorphism to
        change spin to 'Slightly Elliptical' also adds an attribute for Name, for nice print statements """
    def __init__(self,name,distance_au,orbit_average):
        super().__init__(distance_au,"Slightly Elliptical",orbit_average)
        self.name=name

class Comets(SolarObject):
    """ Performs the same as the Planets class"""
    def __init__(self,name,distance_au,orbit_average):
        super().__init__(distance_au,"Like Crazy",orbit_average)
        self.name=name

    def years(self):
        """ Added a method to calculate the years for the orbit time of comets instead of days. """
        years_conversion = self.orbit_average/365.25
        return round(years_conversion,2)


# Variables storing the values for the planets and comets.
earth = Planets("Earth", 1, 360)
mars = Planets("Mars", 1.52, 687)

halley = Comets("Halley Comet",35.143,27375)
hale_bopp = Comets("Hale Bopp",354,863000)

#Lists to allow for less print statements
planetary_objects = [earth, mars]
celestial_rocks = [halley, hale_bopp]

for p in planetary_objects: # Cycles through the list of planets and prints in a formated manner for each planet.
    print(f"Name: {p.name}\n"
          f"Spins: {p.spin}\n"
          f"Supported Population: {p.colonization():,.2f}\n"
          f"Orbit Time: {p.orbit_average} days\n")
for c in celestial_rocks:
    print(f"Name: {c.name}\n"
          f"Spins: {c.spin}\n"
          f"Supported Population: {c.colonization():,.2f}\n"
          f"Orbit Time: {c.years():,.2f} years\n")