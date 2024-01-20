import resources.Font.Font as Font
import resources.Frease.Frease as Frease

def sayhi():
    print('hi')

def saybye():
    print('bye')

def setup():
    window = Font.window()

    inject_tab = window.new_tap('inject')

    top_label = inject_tab.new_label('top_label')
    button = inject_tab.new_button('say hi',sayhi)

    frease_tab = window.new_tap('frease')
    button = frease_tab.new_button('say bye',saybye)

    window.run()


if __name__ == "__main__":
    setup()