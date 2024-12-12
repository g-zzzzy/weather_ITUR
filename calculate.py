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
from nodes import get_satellite
from nodes import get_station
import itur
from astropy import units as u

def check_int(value):
    ivalue = int(value)
    if ivalue not in [0, 1, 2, 3]:
        raise argparse.ArgumentTypeError(f"Integer parameter must be one of 0, 1, 2, or 3. You entered {value}.")
    return ivalue

# def calculate(specific_day, timestamp):
     
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # step 1: set date and time
    parser.add_argument('specific_day', type=str)
    parser.add_argument('timestamp', type=check_int)
    
    args = parser.parse_args()
    specific_date = args.specific_day
    timestamp = args.timestamp

 
    # step 2: get ground-station list
    stations = get_station.get_station()
    for station in stations:
        lat, lon = station
        print(lat, lon)

    # step 3: get satellite list
    satellites = get_satellite.get_satellite()
    for satellite in satellites:
        lat_sat, lon_sat, h_sat = satellite
        print(lat_sat, lon_sat, h_sat)

    # step 4: compute the elevation angle between satellite and ground stations
    el = itur.utils.elve_angle(stations, satellites)
    print("elevation angle: ")
    for station in stations:
        for satellite in satellites:
            print("station: ", station, "satellite: ", satellite, "ele_angle: ", el[(station, satellite)])

    # step 5: set link parameters
    f = 22.5 * u.GHz    # link frequency
    D = 1.2 * u.m       # antenna diameters
    p = 0.1             # unavailability

    # step 6: get weather index of ground station
    T, P, V_t, dew_2m, tr, hr = get_weather.get_weather_init(specific_date, timestamp, lat, lon)

    # step 7: compute the atmospheric attenuation
    itur.atmospheric_attenuation.compute_atmospheric(p, )









    # lat_sat, lon_sat, h_sat = get_satellite.get_satellite()

    # lat_sta, lon_sta = get_station.get_station()

    # lat = get

    # Ag = calculate_Ag(T, P)
    # As = calculate_As()
    # Ar = calculate_Ar()