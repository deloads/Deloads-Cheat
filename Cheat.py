import resources.Font.Font as Font
import resources.Frease.Frease as Frease

def setup():
    window = Font.window()

    inject_tab = window.new_tap('inject')

    label = inject_tab.new_label('text')
    label = inject_tab.new_label('hi')

    inject_tab = window.new_tap('subject')

    label = inject_tab.new_label('test')
    label = inject_tab.new_label('do')

    window.run()


if __name__ == "__main__":
    setup()