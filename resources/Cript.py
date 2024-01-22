import resources.utils.Cript_utils as cript_utils

def encript(path,key):
    with open(path,"r") as file:
        file = file.read()
    convert = []
    for i in range(len(file)):
        convert.append(ord(file[i]))
    for i in key:
        keys = cript_utils.get_keys(ord(i))
        for j in range(len(convert)):
            char = convert[j]+j
            char = char%256
            convert[j] = keys[char]
    cript_utils.write_bytes_to_file(path,convert)

def decript(path,key):
    key = cript_utils.invertString(key)
    convert = cript_utils.read_bytes_from_file(path)
    convert.reverse()

    for i in key:
        keys = cript_utils.get_keys(ord(i))
        for j in range(len(convert)):
            char = convert[j]
            char = keys.index(char)
            char-=(len(convert)-1-j)
            char = char%256
            convert[j] = char
    convert.reverse()
    string = ""
    for i in convert:
        string+= chr(i)
    with open(path,"w") as file:
        file.write(string)