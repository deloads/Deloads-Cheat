import resources.utils.Cript_utils as cript_utils

def encript(path,key):
    with open(path,"r") as file:
        file = file.read()
    convert = {}
    for i in range(len(file)):
        convert[i] = file[i]
    
    for i in key:
        keys = cript_utils.get_keys(ord(i))
        for j in range(len(convert)):
            char = convert[j]
            convert[j] = chr(keys[ord(char)])
    
    new_file = ""
    for i in range(len(convert)):
        new_file+=convert[i]
    print(new_file)


def decript(path,key):
    print('decript')