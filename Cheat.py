import resources as bulp

def select(value):
    print(value)

def setup():
    window = bulp.window()

    test_tab = window.new_tap('test')

    window.run()


if __name__ == "__main__":
    setup()