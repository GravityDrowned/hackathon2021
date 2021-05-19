import datetime
import time
from datetime import datetime
import pandas as pd
from src.read_savefile import read_save
import requests
import json


server_host = 'https://hackbay-zollhof.postman.co/workspace/Team-Workspace~cf82dd4e-f31b-44e1-814a-b8e0412a0bb8/request/15845341-57dc31f3-783a-4b47-b819-bf237cd413df'


def format_date(date):
    # 2021-05-19T11:34:47.810305Z
    #date_rng = pd.date_range(start='5/10/2021', end='5/17/2021', freq='H')
    #for date in date_rng:
    formatted_date = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + 'T' + str(date.hour) + ':' + str(date.minute) + ':' + str(date.second)
    return formatted_date




def send_to_server(dict):
    gas = dict['gas']
    humidity = dict['humidity']
    air_quality_score = dict['air_quality_score']
    temperature = dict['temperature']
    pressure = dict['pressure']
    altitude = dict['altitude']

    date = format_date(datetime.strptime(dict['date'], '%Y-%m-%d %H:%M:%S.%f'))

    print(gas, humidity, air_quality_score, temperature, pressure, altitude, date)

    server = "http://194.61.20.176"
    url = f"{server}/api/"
    response = requests.get(url=url)
    print(response.json())

    # post
    url = f"{server}/api/log/"
    # Temp
    response = requests.post(url=url, json=[{"timestamp": date, "sensor_value": temperature, "area":  "c2cec7ca-7fb6-4f73-b6d0-9456fa038576", "sensor": "38d34757-f7b8-4100-bd3d-20b30433cfdb"}])
    # MOIS
    response = requests.post(url=url, json=[{"timestamp": date, "sensor_value": humidity, "area":  "c2cec7ca-7fb6-4f73-b6d0-9456fa038576", "sensor": "38d34757-f7b8-4100-bd3d-20b30433cfdb"}])
    # IAQ
    response = requests.post(url=url, json=[{"timestamp": date, "sensor_value": air_quality_score, "area":  "c2cec7ca-7fb6-4f73-b6d0-9456fa038576", "sensor": "38d34757-f7b8-4100-bd3d-20b30433cfdb"}])

    print(response.json())


if __name__ == "__main__":
    dict = {
        "area": "c2cec7ca-7fb6-4f73-b6d0-9456fa038576",
        "sensor": "38d34757-f7b8-4100-bd3d-20b30433cfdb",
        "sensor_value": 26,
        "timestamp": "2021-05-19T11:34:47.810305Z"
    }

    data_dict = read_save()
    for dict in data_dict:
        send_to_server(dict)

