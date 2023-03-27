import time
from datetime import datetime, timezone, timedelta
from calendar import monthrange
import numpy as np

print("importing weather module")

pi = 3.1415926535

def subtract_lists(list1,list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    subtracted_array = np.subtract(array1,array2)
    subtracted = list(subtracted_array)
    return subtracted

def interp_1d(x1,x2,y1,y2,x_in,absolute=False):
    x = x1 + (x2 - x1) * x_in
    y = y1 + (x-x1) * ((y2-y1)/(x2-x1))
    return y

class WeatherData:
    def __init__(self):
        self.data = []
        print("building weather Data")

class weather:
    def __init__(self):
        self.data = []
        self.temp = 0
        self.temp_max = [78, 81, 83, 87, 91, 93, 94, 94, 93, 89, 84, 80]
        self.temp_min = [36, 40, 45, 52, 60, 67, 69, 69, 65, 54, 43, 39]
        self.temp_amp = subtract_lists(self.temp_max,self.temp_min)
        self.year = 0
        self.month = 0
        self.day = 0
    
    def interpolate_time(self,time_epoch):
        dt_obj  = datetime.fromtimestamp(time_epoch,timezone.utc)
        dt_tup = dt_obj.timetuple()
        self.year = dt_tup[0]
        self.month = dt_tup[1]
        self.day = dt_tup[2]
        dt_obj0 = datetime(self.year,self.month,self.day,0,0,0,0,timezone.utc)
        day_seconds = dt_obj - dt_obj0
        day_seconds = day_seconds.total_seconds()
        days_in_month = monthrange(self.year,self.month)
        days_in_month = days_in_month[1]
        #day_f = day_seconds / 86400
        # print("dayf = " + str(day_f))
        month_f = self.day / days_in_month
        # print("month_f = " + str(month_f))
        return [month_f,day_seconds]
    
    def CalcSinParam(self,tempH,tempL):
        wxA  = (tempH - tempL) / 2
        wxD = (tempH + tempL) / 2
        # Frequency: T = 2pi/omega
        # omega = 2pi / T
        # T = 1 day or 86400 seconds
        wxB = (2 * pi) / (86400)
        wxC = pi
        print("wxA " + str(wxA))
        print("wxB " + str(wxB))
        print("wxC " + str(wxC))
        print("wxD " + str(wxD))
        return [wxA,wxB,wxC,wxD]

    def CalcTemp(self,time):
        [month_f,day_seconds] = self.interpolate_time(time)
        # Get high/low Temp for the day
        if self.month == 12:
            tempH = interp_1d(0,1,self.temp_max[self.month-1],self.temp_max[0],month_f)
            tempL = interp_1d(0,1,self.temp_min[self.month-1],self.temp_min[0],month_f)
        else :
            tempH = interp_1d(0,1,self.temp_max[self.month-1],self.temp_max[self.month],month_f)
            tempL = interp_1d(0,1,self.temp_min[self.month-1],self.temp_min[self.month],month_f)
        print("High: " + str(tempH) + " Low: " + str(tempL))
        # y = A * cos(Bx + C) + D
        [wxA,wxB,wxC,wxD] = self.CalcSinParam(tempH,tempL)
        self.temp = wxA * np.cos(wxB * day_seconds - wxC) + wxD
        print()
        print("Time of day (seconds): " + str(day_seconds))
        print("Calculated Temp: " + str(self.temp))
        return self.temp



w = weather()
#w.CalcTemp(time.time())
w.CalcTemp(1671978321)