import random
from astropy import units as u



def get_satellites_data(num_satellites=100):
    satellites = []
    lat = 30.5
    lon = 103.5
    h = 500 * u.km
    satellites.append((lat, lon, h))
    
    return satellites


def get_satellite():
    satellites = get_satellites_data()
    return satellites


