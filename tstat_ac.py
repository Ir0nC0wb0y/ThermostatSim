

ac_capacity     = 36000 # [btu/hr]
heater_capacity = 50000 # [btu/hr]


class ac:
    def __init__(self):
        self.state_ac = 0
        self.powerAC = ac_capacity / 3.41 # W
        self.powerHEAT = heater_capacity / 3.41 # W

    def update(self,state_ac,display = 0):
        match state_ac:
            case "heat":
                self.state_ac = self.powerHEAT
            case "cool":
                self.state_ac = -1 * self.powerAC
            case _:
                self.state_ac = 0
        if display == 1:
            print("AC Power: " + str(self.state_ac))
