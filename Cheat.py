import resources as bulp

def encript():
    bulp.encript("data/test.json","key1")

def decript():
    bulp.decript("data/test.json","key1")

def setup():
    window = bulp.window()

    cript_tap = window.new_tap('cript')
    encript_button = cript_tap.new_button('encript',encript)
    decript_button = cript_tap.new_button('decript',decript)

    window.run()


if __name__ == "__main__":
    setup()