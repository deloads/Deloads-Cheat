import resources.Font.Font as Font
import resources.Frease.Frease as Frease

def sayhi():
    print('hi')

def saybye():
    print('bye')

def toggle(value):
    print(value)

def setup():
    window = Font.window()

    test_tab = window.new_tap('test')
    slider = test_tab.new_slider('slider',[2,10,5],10)

    window.run()


if __name__ == "__main__":
    setup()