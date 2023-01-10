from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button as Btn
from tkinter import filedialog

# Main screen for Music Player
musicPlayer = Tk()
musicPlayer.title("Reese Music Player")

#--------------------------------------------------------LABLE-------------------------------------------------------

#Labels
Label(musicPlayer,text="Custom Music Player",font=("Calibri",15), fg="Red").grid(sticky="N",row=0,padx=120)
Label(musicPlayer,text="Select Track",font=("Calibri",12), fg="blue").grid(sticky="N",row=1)
Label(musicPlayer,text="Volume",font=("Calibri",12), fg="red").grid(sticky="N",row=4)

#Track Title
Track_Label = Label(musicPlayer,font=("Calibri", 4))
Track_Label.grid(stick="N",row=3)

#Volume
volumeLable = Label(musicPlayer,font=("Calibri",13))
volumeLable.grid(sticky="N",row=5)

#Buttons
Btn(musicPlayer, text="Select Track", font=("Calibri", 12)).grid(row=2,sticky="N")
Btn(musicPlayer, text="Pause", font=("Calibri",12)).grid(row=3,sticky="E")
Btn(musicPlayer, text="Resume", font=("Calibri",12)).grid(row=3,sticky="W")
Btn(musicPlayer, text="-", font=("Calibri",12),width=5).grid(row=5,sticky="W")
Btn(musicPlayer, text="+", font=("Calibri",12),width=5).grid(row=5,sticky="E")

#--------------------------------------------------------LABLE-------------------------------------------------------

musicPlayer.mainloop()