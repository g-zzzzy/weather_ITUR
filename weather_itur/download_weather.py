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
import shutil
import time

def download_era5_data(date_str):
    c = cdsapi.Client()
    # 2m temperature
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': '167',
        'time': '00/to/23/by/6',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/T.nc')
    
    # surface pressure
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': '134',
        'time': '00/to/23/by/6',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/P.nc')
    
    # total column water vapour
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': '137',
        'time': '00/to/23/by/6',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/V_t.nc')

    # # specific humidity
    # 用2m露点温度和2m气压算
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': '168',
        'time': '00/to/23/by/6',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/dew_T.nc')
    
    # mean total precipitation rate
    # download the precipitation data for the given day
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': era5_precipitation_code,
        'time': '00/to/23/by/1',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/precipitation.nc')

    
    # cloud base height
    c.retrieve('reanalysis-era5-single-levels', {
        'date': date_str,
        'product_type': 'reanalysis',
        'param': '228023',
        'time': '00/to/23/by/6',
        'grid': prod_model_grid,
        'format': 'netcdf',
    }, f'{save_dir}/{date_str}/hr.nc')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('start_date', type=str)
    parser.add_argument('end_date', type=str)
    
    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date

    for date in pd.date_range(start_date, end_date):
        print(date)
        date_str = date.strftime('%Y-%m-%d')
        folder_path = f'{save_dir}/{date_str}'
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.mkdir(folder_path)
        start_time = time.time()
        download_era5_data(date_str)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")