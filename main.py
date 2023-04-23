import time
from datetime import datetime
from tstat_weather import weather
from tstat_home import home

# Environment
home_size            = 1800 # [square feet]
home_avg_ceiling_hgt =    8 # [feet]

h = home(home_size*home_avg_ceiling_hgt,75)

w = weather()
env_temp = w.CalcTemp(time.time())
#env_temp = w.CalcTemp(1671978321)
print("Calculated Temp: " + str(env_temp))

h.update()