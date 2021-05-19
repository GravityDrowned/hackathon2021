from src.read_savefile import read_save
from src.server_interface import send_to_server

import pandas as pd
from datetime import datetime
import numpy as np
#import datetime
import random




# ok
# 2021-05-19 00:24:21.514609
# to
# 2021-05-20 12:49:0.514609

def pick_close_values(data_dict, scramble_date):
    for dict in data_dict:
        date = datetime.strptime(dict['date'], '%Y-%m-%d %H:%M:%S.%f')

        if (scramble_date.hour > date.hour):
            #print(scramble_date.hour, '>', date.hour, scramble_date.hour > date.hour, date)

            air_qu_noise = random.uniform(0, 1) - 0.5

            #temp_noise = \sin(x\cdot\frac{1}{2}+10)\
            x = date.hour
            temp_noise = np.sin(x/2 + 10)
            gas = dict['gas'] + air_qu_noise * dict['gas']
            humidity = dict['humidity'] + air_qu_noise * dict['humidity']
            air_quality_score = dict['air_quality_score'] + air_qu_noise * dict['air_quality_score']
            temperature = dict['temperature']+ temp_noise * dict['temperature']
            pressure = dict['pressure']
            altitude = dict['altitude']

            scramble_dict = {
                "gas": gas,
                "humidity": humidity,
                "air_quality_score": air_quality_score,
                "temperature": temperature,
                "pressure": pressure,
                "altitude": altitude,
                "date": date
            }

            return scramble_dict


def scramble(data_dict):
    # for dict in data_dict:
    # some kind of time flow
    # datetime.fromtimestamp(time.time())
    date_rng = pd.date_range(start='5/10/2021', end='5/17/2021', freq='H')
    for d in date_rng:
        # print(d)
        scramble_dict = pick_close_values(data_dict, d)
        print(scramble_dict)

        for s in scramble_dict:
            send_to_server(s)


    # sinus curves?
    # read data and noise


if __name__ == "__main__":
    data_dict = read_save()
    scramble(data_dict)
