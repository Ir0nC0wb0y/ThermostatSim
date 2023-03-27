import time
from datetime import datetime
from tstat_weather import weather


w = weather()
env_temp = w.CalcTemp(time.time())
#env_temp = w.CalcTemp(1671978321)
print("Calculated Temp: " + str(env_temp))