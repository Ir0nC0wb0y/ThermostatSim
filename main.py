import time
from datetime import datetime
from tstat_weather import weather
from tstat_home import home
from tstat_ac import ac
from tstat_tstat import tstat as t



w  = weather()
h  = home(71.0)
ac = ac()
tstat = t()

sim_time = 0
while sim_time < 500:
    #w.CalcTemp(time.time(),1)
    w.CalcTemp(1671978321 + sim_time)
    tstat.update(h.state.temp)
    ac.update(tstat.state_ac)
    h.update(w.temp,ac.state_ac)
    sim_time = sim_time + 1
    #print("sim_count: " + str(sim_time))
    #print()
    print(str(sim_time) + ", " + str(tstat.state_ac) + ", " + str(ac.state_ac) + ", " + str(h.Qtot) + ", " + str(h.state.temp))
    