

ac_size = 36000 # [btu/hr]


class tstat:
    def __init__(self):
        self.state_ac = 0
        self.power = ac_size / 3.41 # W

    def state_ac(self,state_ac):
        match state_ac:
            case "heat":
                self.state_ac = self.power
            case "cool":
                self.state_ac = -1 * self.power
            case _:
                self.state_ac = 0
