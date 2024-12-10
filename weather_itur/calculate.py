import cdsapi
import datetime
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from glob import glob
import argparse
import os
import threading
import get_weather
import get_satellite

def check_int(value):
    ivalue = int(value)
    if ivalue not in [0, 1, 2, 3]:
        raise argparse.ArgumentTypeError(f"Integer parameter must be one of 0, 1, 2, or 3. You entered {value}.")
    return ivalue

def calculate(specific_day, timestamp):
    #read P
    P = Dataset(f'{save_dir}/{specific_day}/P.nc')
    longitude = P['longitude'][:]
    latitude = P['latitude'][:]
    time = P['valid_time'][:]
    print(time)
    
    # # 获取所有的变量（variables）名称
    # variables = P.variables

    # #   输出变量名称的 dict_keys 格式
    # print(dict(variables).keys())
    
    #print()
    # 单位已转成hPa
    unique_lat = np.unique(latitude)
    unique_lon = np.unique(longitude)
    for t in range(len(time)):
        for lat in range(len(unique_lat)):
            for lon in range(len(unique_lon)):
                sp_value = P['sp'][t, lat, lon] / 100
                print(f"Time {time[t]}, Latitude {unique_lat[lat]}, Longitude {unique_lon[lon]}, Pressure {sp_value}")  
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('specific_day', type=str)
    parser.add_argument('timestamp', type=check_int)
    parser.add_argument('lat', type=float)
    parser.add_argument('lon', type=float)
    
    args = parser.parse_args()
    specific_date = args.specific_day
    timestamp = args.timestamp
    lat = args.lat
    lon = args.lon

    # weather index of specific date at specific (lat, lon, timestamp)
    # timestamp : 0, 1, 2, 3
    T, P, V_t, dew_2m, tr, hr = get_weather.get_weather_init(specific_date, timestamp, lat, lon)

    lat_sat, lon_sat, h_sat = get_satellite.get_satellite()

    lat = get

    Ag = calculate_Ag(T, P)
    As = calculate_As()
    Ar = calculate_Ar()