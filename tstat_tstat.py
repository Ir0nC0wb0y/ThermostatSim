

class tstat:
    def __init__(self,set_point):
        self.set_point  = set_point
        #self.state_fan = "off" # this is not necessary until hotspots can occur in home model
        self.state_ac  = "off"
        self.mode      = "ac"
    
    def calcState(self,currentTemp):
        match self.mode:
            case "ac":
                #do ac stuff
                if currentTemp > self.set_point:
                    self.state_ac = "cool"
                else:
                    self.state_ac = "off"
            case "heat":
                #do heat stuff
                if currentTemp < self.set_point:
                    self.state_ac = "heat"
                else:
                    self.state_ac = "off"
            case _:
                #turn off ac
                self.state_ac = "off"