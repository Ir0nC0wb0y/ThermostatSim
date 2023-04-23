import random

air_specific_heat = 1 # [J/gK]
air_density = 1275 # [g/m3]

print("importing home module")

class home_state:
    def __init__(self):
        self.temp = 70

    def updateTemp(self,newTemp):
        self.temp = newTemp

class home:
    def __init__(self,air_vol,initial_temp):
        self.state = home_state()
        self.air_mass = air_vol * 0.0283168 * air_density # ft3 * m3/ft3 * g/m3 = g
        print("Air mass: " + str(self.air_mass))
        self.temp = initial_temp
    
    def update(self):
        self.state.updateTemp(random.randrange(60,86))
        print("New Temperature: " + str(self.state.temp))
        

    # Functional needs:
        # heat in (based on time @ temp)
        # heat out