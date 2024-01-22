import json

all_keys = 1

def get_keys(stroke):
    global all_keys
    if all_keys == 1:
        with open("data/.keys.json") as file:
            all_keys = json.load(file)
    return all_keys[stroke]