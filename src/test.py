import os
from tkinter import *

# from Tkinter import *

app = Tk()
app.title('Audio Player')

Fcanvas = Canvas(bg='black', height=600, width=600)

def snd1():
  os.system("D:\GitHub\BCI\sampleaudio1.wav")

def snd2():
  os.system("D:\GitHub\BCI\sampleaudio2.wav")


var = IntVar()

rb1 = Radiobutton(app, text = "Play audio one", variable = var, value = 1, command= snd1)
rb1.pack(anchor= W)
rb2 = Radiobutton(app, text = "Play audio two", variable = var, value = 1, command= snd2)
rb2.pack(anchor= W)

Fcanvas.pack()
app.mainloop( )