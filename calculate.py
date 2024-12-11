import cdsapi
import datetime
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from glob import glob
import argparse
import os
import threading
from weather import get_weather
import itur

def check_int(value):
    ivalue = int(value)
    if ivalue not in [0, 1, 2, 3]:
        raise argparse.ArgumentTypeError(f"Integer parameter must be one of 0, 1, 2, or 3. You entered {value}.")
    return ivalue

# def calculate(specific_day, timestamp):
     
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('specific_day', type=str)
    parser.add_argument('timestamp', type=check_int)
    parser.add_argument('lat', type=float)
    parser.add_argument('lon', type=float)
    # parser.add_argument('sat_num', type=int)
    # parser.add_argument('station_num', type=int)
    
    args = parser.parse_args()
    specific_date = args.specific_day
    timestamp = args.timestamp
    lat = args.lat
    lon = args.lon
    # sat_num = args.sat_num
    # station_num = args.station_num

    # weather index of specific date at specific (lat, lon, timestamp)
    # timestamp : 0, 1, 2, 3
    T, P, V_t, dew_2m, tr, hr = get_weather.get_weather_init(specific_date, timestamp, lat, lon)

    # print(T, P , V_t)

    # ########################### #
    # test case'

    # test ground-station
    lat = 39.9
    lon = 116.4

    # test satellite
    lat_sat = 30.5 # N o
    lon_sat = 103.5 # E o
    h_sat = 500 * itur.u.km # km




    # lat_sat, lon_sat, h_sat = get_satellite.get_satellite()

    # lat_sta, lon_sta = get_station.get_station()

    # lat = get

    # Ag = calculate_Ag(T, P)
    # As = calculate_As()
    # Ar = calculate_Ar()