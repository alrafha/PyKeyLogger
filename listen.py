from pynput.mouse import Listener

def readmouseloc(x,y):
    print("Position of current mouse {0}".format((x,y)))


with Listener(on_move=readmouseloc) as l:
    l.join()