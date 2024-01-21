import resources as bulp

def sayhi():
    print('hi')

def setup():
    window = bulp.window()

    test_tab = window.new_tap('test')
    entry = test_tab.new_entry('some text')
    def click():
        print(entry.get_number())
    button = test_tab.new_button('value?',click)

    window.run()


if __name__ == "__main__":
    setup()