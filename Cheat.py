import resources as bulp

def encript():
    bulp.encript("data/test.json","awbdgu7iaw")

def decript():
    bulp.decript("data/test.json","awbdgu7iaw")

def setup():
    window = bulp.window()

    cript_tap = window.new_tap('cript')
    encript_button = cript_tap.new_button('encript',encript)
    decript_button = cript_tap.new_button('decript',decript)
    
    return window

if __name__ == "__main__":
    setup().run()