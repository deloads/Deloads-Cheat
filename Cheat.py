import env.Font.Font as Font
import env.Frease.Frease as Frease

def setup():
    window = Font.window()

    inject_tab = window.new_tap('inject')

    window.run()


if __name__ == "__main__":
    setup()