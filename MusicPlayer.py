from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button as Btn
from tkinter import filedialog

# Main screen for Music Player
musicPlayer = Tk()
musicPlayer.title("Reese Music Player")

#--------------------------------------------------------COMMANDS-------------------------------------------------------
#Volume control
volumeControl = float(0.5) 

#This will play the track file that is stored on the device
def playTrack():
    fileName  = filedialog.askopenfile(initialdir="E:/", title="Please Select File")
    currentTrack = fileName
#==========FIX IN THE FUTURE====================
    # trackName = fileName.split("/")
    # trackName = trackName[-1]
#==========FIX IN THE FUTURE====================
    print(fileName)

    try:
        mixer.init()
        mixer.music.load(fileName)
        mixer.music.set_volume(volumeControl)
        mixer.music.play()
        Track_Label.config(fg="blue",text="Now Playing : " + str(fileName) )
        volumeLable.config(fg="black",text="Volume: " + str(volumeControl))
    except Exception as e:
        print(e)
        Track_Label.config(fg="black", text="Error playing track")

def reduceSound():
    try:
        global volumeControl
        if volumeControl <= 0:
            volumeLable.config(fg="red", text="Volume : Muterd")
            return
        volumeControl = volumeControl - float(0.1)
        volumeControl = round(volumeControl, 1)
        mixer.music.set_volume(volumeControl)
        volumeLable.config(fg="green", text="Volume : " + str(volumeControl))
    except Exception as e:
        print(e)
        Track_Label.config(fg="Red", text="Track isn't selected")

def increaseVolume():
    try:
        global volumeControl
        if volumeControl >= 1:
            volumeLable.config(fg="Green", text="Volume : Max")
            return
        volumeControl = volumeControl + float(0.1)
        volumeControl = round(volumeControl, 1)
        mixer.music.set_volume(volumeControl)
        volumeLable.config(fg="green", text="Volume : " + str(volumeControl))
    except Exception as e:
        print(e)
        Track_Label.config(fg="Red", text="Track isn't selected")





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
Btn(musicPlayer, text="Select Track", font=("Calibri", 12),command=playTrack).grid(row=2,sticky="N")
Btn(musicPlayer, text="Pause", font=("Calibri",12)).grid(row=3,sticky="E")
Btn(musicPlayer, text="Resume", font=("Calibri",12)).grid(row=3,sticky="W")
Btn(musicPlayer, text="-", font=("Calibri",12),width=5, command=reduceSound).grid(row=5,sticky="W")
Btn(musicPlayer, text="+", font=("Calibri",12),width=5, command=increaseVolume).grid(row=5,sticky="E")




musicPlayer.mainloop()