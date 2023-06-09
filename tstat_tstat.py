

setpoint_default = 70.0
setpoint_buffer  =  1.5

class tstat:
    def __init__(self, Mode = "off"):
        self.set_point  = setpoint_default
        #self.state_fan = "off" # this is not necessary until hotspots can occur in home model
        self.state_ac  = "off"
        self.mode      = Mode
    
    def update(self,currentTemp,display = 0):
        match self.mode:
            case "ac":
                #do ac stuff
                if currentTemp > self.set_point + setpoint_buffer:
                    self.state_ac = "cool"
                elif currentTemp < self.set_point:
                    self.state_ac = "off"
            case "heat":
                #do heat stuff
                if currentTemp < self.set_point - setpoint_buffer:
                    self.state_ac = "heat"
                elif currentTemp > self.set_point:
                    self.state_ac = "off"
            case "auto":
                if self.state_ac == "off" and currentTemp > self.set_point + setpoint_buffer:
                    self.state_ac = "cool"
                elif self.state_ac == "off" and currentTemp < self.set_point - setpoint_buffer:
                    self.state_ac = "heat"
                elif self.state_ac == "cool" and currentTemp <= self.set_point:
                    self.state_ac = "off"
                elif self.state_ac == "heat" and currentTemp >= self.set_point:
                    self.state_ac = "off"
                #else:
                #    self.state_ac = "off"
            case "smart":
                pass
            case _:
                #turn off ac
                self.state_ac = "off"
        if display == 1:
            print("tstat state: " + self.state_ac)

    def setPoint(self,setpoint):
        self.set_point = setpoint

    def setMode(self,Mode):
        self.mode = Mode