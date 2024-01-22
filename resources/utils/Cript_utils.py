import json

all_keys = 1

def get_keys(stroke):
    global all_keys
    if all_keys == 1:
        with open("data/.keys.json") as file:
            all_keys = json.load(file)
    return all_keys[stroke]

def write_bytes_to_file(file_path, byte_list):
    with open(file_path, 'wb') as file:
        file.write(bytes(byte_list))

def read_bytes_from_file(file_path):
    with open(file_path, 'rb') as file:
        byte_data = file.read()
        byte_list = list(byte_data)
    return byte_list

def invertString(string):
    newString = string[::-1]
    return newString
