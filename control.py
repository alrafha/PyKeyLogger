# from pynput.mouse import Controller

from pynput.keyboard import Controller


def mousecontroller():
    mouse = Controller()
    mouse.position = (250,650) # The values will place the mouse pointer to the given position condidering from axes from 
                            # top-left corner of the screen

# mousecontroller()

def keyboardcontroller():
    keyboard = Controller()
    keyboard.type("I am Hamza")

keyboardcontroller()

# Just a sample text: I am Hamza