import time
import pyautogui
import tkinter as bhardwaj

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root =bhardwaj.Tk()
frame = bhardwaj.Frame(root)
frame.pack()

button =bhardwaj.Button(
    frame,
    text = "Take Screenshot",
    command=screenshot)

button.pack(side=bhardwaj.LEFT)
close=bhardwaj.Button(
    frame,
    text = "Quit",
    command=quit)

close.pack(side=bhardwaj.LEFT)

root.mainloop()