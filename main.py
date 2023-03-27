from time import gmtime, strftime
#import tstat_weather
from datetime import datetime
#w = weather()

dt_obj = datetime.now()
dt_tup = dt_obj.timetuple()
year = dt_tup[0]
month = dt_tup[1]
day = dt_tup[2]
print(str(year) + "/" + str(month) + "/" + str(day))