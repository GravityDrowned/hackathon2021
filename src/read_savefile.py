# I created data over night, saved it locally
# This is supposed to read it and send it to the API provided by Subrahmanya

# mqtt
# adastuff
# netatmo - https://www.amazon.de/-/en/Netatmo-quality-temperature-humidity-sensors/dp/B01LZAZ4LS

import json
import ast


def read_save():
    dict_list = []
    path = './data/data_michaels_night.json'
    # savefile = json.load(path)

    # Using readlines()
    savefile = open(path, 'r')
    lines = savefile.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        dict = ast.literal_eval(line)
        #print(dict)
        dict_list.append(dict)

    return dict_list


if __name__ == "__main__":
    savefile = read_save()
    for save in savefile:
        print(save)
        #send_to_server(save)
