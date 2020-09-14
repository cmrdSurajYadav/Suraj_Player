from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import playsound
from tkinter.ttk import Progressbar
from pygame import *
mixer.init()
f=""
def s_button():
    f=filedialog.askopenfilename(type=('mp3','mp4','wav'))
    print(f)
    tr.set(f)


    
def play():
    try:
        mixer_music.load(tr.get())
        mixer_music.play()
        # Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
        play_button=ttk.Button(l,text="stop",image=stop_icon,command=stop).place(x=190,y=385)
        pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)
        tr1=StringVar()
        tr1.set("select song for play")
        tract=Entry(l,font=("Times", "24", "bold italic"),textvariable=tr)
        tract.place(x=100,y=330)
        ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
        ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)
        logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
        logo2.place(x=120,y=10)
        v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)
        v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
    except:
        messagebox.showerror("Not Found","please Select currect file")

    
def stop():
    mixer_music.stop()
    Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
    # play_button=ttk.Button(l,text="stop",image=stop_icon,command=stop).place(x=190,y=385)
    pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)
    tr=StringVar()
    tr.set("select song for play")
    tract=Entry(l,font=("Times", "24", "bold italic"),textvariable=tr)
    tract.place(x=100,y=330)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)
    logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
    logo2.place(x=120,y=10)
    v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)

    v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
def pause():
    mixer_music.pause()
    resume_button=ttk.Button(l,text="resume",image= resume_icon,command=resume).place(x=190,y=385)
    Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
#    play_button=ttk.Button(l,text="stop",image=stop_icon,command=stop).place(x=190,y=385)
    # pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)
    tr=StringVar()
    tr.set("Click Resume For Resume The Music")
    tract=Entry(l,font=("Times", "24", "bold italic"),textvariable=tr)
    tract.place(x=100,y=330)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)
    v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)

    v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
    logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
    logo2.place(x=120,y=10)

def resume():
    
    mixer_music.unpause()
    # Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
    play_button=ttk.Button(l,text="stop",image=stop_icon,command=stop).place(x=190,y=385)
    pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)
    
    tr=StringVar()
    tr.set("click pause for pause the music")
    tract=Entry(l,font=("Times", "24", "bold italic"),textvariable=tr)
    tract.place(x=100,y=330)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)
    v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)
    v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
    logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
    logo2.place(x=120,y=10)
def vvup():
    v=mixer_music.get_volume()
    mixer_music.set_volume(v+0.1)
    p=mixer_music.get_volume()*100
    logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
    logo2.place(x=120,y=10)
   
    
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
# play_icon=PhotoImage(file="play.png")
    plays_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)

    Stop_button=ttk.Button(l,text="Stop",image= stop_icon,command=stop).place(x=190,y=385)
    # play_button=ttk.Button(l,text="stop",image=play_icon,command=play).place(x=190,y=385)
    pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)

    v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)

    v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
   
    progress = Progressbar(l, orient = VERTICAL, 
              length = 100, mode = 'determinate',maximum=100,value=p) 
    progress.place(x=400, y=100)
    progress.update()
def vvdwn():
    v=mixer_music.get_volume()
    mixer_music.set_volume(v-0.1)

    p=mixer_music.get_volume()*100
    logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
    logo2.place(x=120,y=10)
   
    
    ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
# play_icon=PhotoImage(file="play.png")
    plays_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)

    Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
    # play_button=ttk.Button(l,text="stop",image=play_icon,command=play).place(x=190,y=385)
    pouse_button=ttk.Button(l,text="Pause",image= pasuse_icon,command=pause).place(x=290,y=385)

    v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)

    v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)
    
    progress.update()

root=Tk()
root.geometry("533x444")
root.title("suraj music player")
logo=PhotoImage(file='—Pngtree—enjoying listening to music_5424708.png')
l=Label(root,image=logo)
l.pack()
logo2=Label(l,text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
logo2.place(x=120,y=10)
tr=StringVar()
tr.set("S:/ok/hai mera dil1_(PagalWorld.com).mp3")
tract=Entry(l,font=("Times", "24", "bold italic"),textvariable=tr)
tract.place(x=100,y=330)
play_icon=PhotoImage(file="d.png")
search_icon=PhotoImage(file="do.png")
stop_icon=PhotoImage(file="stop.png")
pasuse_icon=PhotoImage(file="pause.png")
resume_icon=PhotoImage(file="images.png")
up=PhotoImage(file="up.png")
down=PhotoImage(file="down.png")

ser_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=40,y=335)
# play_icon=PhotoImage(file="play.png")
plays_button=ttk.Button(l,text="Search ",image= search_icon,command=s_button).place(x=450,y=335)

Stop_button=ttk.Button(l,text="Stop",image= play_icon,command=play).place(x=190,y=385)
# play_button=ttk.Button(l,text="stop",image=play_icon,command=play).place(x=190,y=385)
resume_button=ttk.Button(l,text="resume",image= resume_icon,command=resume).place(x=290,y=385)

v_up=ttk.Button(l,text="Volume Up",image=up,command=vvup).place(x=390,y=385)

v_dp=Button(l,text="Volume Down",image=down, command=vvdwn).place(x=100,y=385)





root.mainloop()