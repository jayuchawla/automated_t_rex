from PIL import ImageGrab,ImageOps
import numpy as np
import pyautogui
import time

class coordinate():
    replaybutton = (684,384)
    dinosaur = (445,393)

def restart():
    pyautogui.click(coordinate.replaybutton)

def spacepress():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def boxgrab():
    box = (coordinate.dinosaur[0]+20,coordinate.dinosaur[1],coordinate.dinosaur[0]+100,coordinate.dinosaur[1]+23 )
    img = ImageGrab.grab(box)
    grayimg = ImageOps.grayscale(img)
    a = np.array(grayimg.getcolors())
    return(np.sum(a))

def main():
    time.sleep(5)          
    restart()
    
    while True:
        print(boxgrab())
        if boxgrab()!=2087:
            spacepress()
            time.sleep(0.1)

main()