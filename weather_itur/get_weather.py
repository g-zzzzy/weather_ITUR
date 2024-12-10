import cdsapi
import datetime
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from glob import glob
import argparse
import os
from constant import *
import threading
from datetime import datetime

def check_int(value):
    ivalue = int(value)
    if ivalue not in [0, 1, 2, 3]:
        raise argparse.ArgumentTypeError(f"Integer parameter must be one of 0, 1, 2, or 3. You entered {value}.")
    return ivalue
    
def get_weather(folder_path, timestamp, lat, lon):
    T_Dataset = Dataset(f'{folder_path}/T.nc')
    T = T_Dataset['t2m'][timestamp, lat, lon]   #   K

    P_Dataset = Dataset(f'{folder_path}/P.nc')
    P = P_Dataset['sp'][timestamp, lat, lon] / 100  # hPa

    V_t_Dataset = Dataset(f'{folder_path}/V_t.nc')
    V_t = V_t_Dataset['tcwv'][timestamp, lat, lon]  #   kg/m2

    dew_2m_Dataset = Dataset(f'{folder_path}/dew_T.nc')
    dew_2m = dew_2m_Dataset['d2m'][timestamp, lat, lon] #   K

    # 6h内的平均每秒降水
    tr_Dataset = Dataset(f'{folder_path}/tr.nc')
    tr = tr_Dataset['precip_6hr'][timestamp, lat, lon] / 6  #   kg/m2/s = mm/s

    hr_Dataset = Dataset(f'{folder_path}/hr.nc')
    hr = hr_Dataset['cbh'][timestamp, lat, lon] / 1000   #   km

    return T, P, V_t, dew_2m, tr, hr

def get_weather_init(specific_date, timestamp, lat, lon):
    specific_date = datetime.strptime(specific_date, '%Y-%m-%d')
    date_str = specific_date.strftime('%Y-%m-%d')
    folder_path = f'{save_dir}/{date_str}'

    if os.path.exists(folder_path):
        # print("downloaded")
        T, P, V_t, dew_2m, tr, hr = get_weather(folder_path, timestamp, lat, lon)
        return T, P, V_t, dew_2m, tr, hr
    else:
        print("not downloaded")



        
        
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
    get_weather_init(specific_date, timestamp, lat, lon)


