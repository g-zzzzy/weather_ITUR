import random

# 生成100个卫星的经纬度和高度
def generate_satellite_data(num_satellites=100):
    satellites = []
    for i in range(num_satellites):
        # 随机生成纬度 (-90 to 90)
        lat = round(random.uniform(-90, 90), 6)
        # 随机生成经度 (-180 to 180)
        lon = round(random.uniform(-180, 180), 6)
        # 随机生成卫星高度 (300 km to 2000 km)
        altitude = round(random.uniform(300, 2000), 2)
        
        satellites.append((lat, lon, altitude))
    
    return satellites


def get_satellite():
    satellites = generate_satellite_data()
    first_satellite = satellites[0]
    lat, lon, h = first_satellite
    return lat, lon, h


