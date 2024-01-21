import resources as bulp

def sayhi():
    print('hi')

def saybye():
    print('bye')

def toggle(value):
    print(value)

def slide(value):
    print(value)

def setup():
    window = bulp.window()

    test_tab = window.new_tap('test')
    slider = test_tab.new_slider('slider',[0,10],0)

    window.run()


if __name__ == "__main__":
    setup()