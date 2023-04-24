import time
from datetime import datetime
from tstat_weather import weather
from tstat_home import home
from tstat_ac import ac
from tstat_tstat import tstat as t



w  = weather()
h  = home(71.0)
ac = ac()
tstat = t("auto")

file_header = "Sim Time, Enviro Temp, Tstat State, AC Heat, Total Heat, New Temp"
print(file_header)

f = open("sim-run.csv","w")
f.write(file_header + "\n")
sim_time = 0
sim_period = 10
while sim_time < 2592000:
    #w.CalcTemp(time.time(),1)
    w.CalcTemp(1689396268 + sim_time)
    tstat.update(h.state.temp)
    ac.update(tstat.state_ac)
    h.update(w.temp,ac.state_ac)
    sim_time = sim_time + sim_period
    #print("sim_count: " + str(sim_time))
    #print()
    csv_line = str(sim_time) +", " + str(w.temp) + ", " + str(tstat.state_ac) + ", " + str(ac.state_ac) + ", " + str(h.Qtot) + ", " + str(h.state.temp)
    print(csv_line)
    f.write(csv_line + "\n")

f.close()
    