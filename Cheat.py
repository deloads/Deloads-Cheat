import resources as bulp
content = {}

def encript():
    key = content["key"].get_string()
    bulp.encript("data/test.json",key)

def decript():
    key = content["key"].get_string()
    bulp.decript("data/test.json",key)

def setup():
    window = bulp.window()

    cript_tap = window.new_tap('cript')
    content['key'] = cript_tap.new_entry("key")
    encript_button = cript_tap.new_button('encript',encript)
    decript_button = cript_tap.new_button('decript',decript)
    
    return window

if __name__ == "__main__":
    setup().run()