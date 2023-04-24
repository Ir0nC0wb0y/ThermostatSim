import random

# Air Attributes
air_specific_heat = 1 # [J/gK]
air_density = 1275 # [g/m3]

# Home Attributes
home_size            = 1800 # [square feet]
home_avg_ceiling_hgt =    8 # [feet]
home_conductivity = 300 # units, also, what should this be?!?! this will influence how fast 

print("importing home module")

class home_state:
    def __init__(self):
        self.temp = 0 # If the temp ever goes to zero indicates an issue

    def updateTemp(self,newTemp):
        self.temp = newTemp

class home:
    def __init__(self,initial_temp):
        air_vol = home_size*home_avg_ceiling_hgt # [ft3]
        self.state = home_state()
        self.air_mass = air_vol * 0.0283168 * air_density # ft3 * m3/ft3 * g/m3 = g
        self.Qtot = 0
        print("Air mass: " + str(self.air_mass))
        self.state.updateTemp(initial_temp)
        print("Initial temp: " + str(self.state.temp))
    
    def update(self,tempEnviro,ac_heat,display = 0):
        #heatEnviro = self.heat_Enviro(self,tempEnviro)
        Qcc = self.heatCC(tempEnviro)
        Qac = ac_heat
        Qrad = self.heatRAD()
        self.Qtot = Qcc + Qac + Qrad
        #print("Total Heat change: " + str(self.Qtot))
        newTemp = (self.Qtot / (air_specific_heat * self.air_mass)) + self.state.temp
        #newTemp = random.randrange(60,86) # once temperature updates correctly, REMOVE THIS LINE
        self.state.updateTemp(newTemp)
        if display == 1:
            print("New Temperature: " + str(self.state.temp))
        
    def heatCC(self,tempEnviro):
        heat_CC = (tempEnviro - self.state.temp) * home_conductivity
        #print("heatCC = " + str(heat_CC))
        return heat_CC
    
    def heatRAD(self,state_rad = 0):
        return 0 # This should be updated with radiation, once Weather model can supply

    # Functional needs:
        # heat in (based on time @ temp)
        # heat out