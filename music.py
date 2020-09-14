from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox,filedialog
from pygame import *
from tkinter import ttk
from mutagen.mp3 import MP3
import datetime
import os
import random

mixer.init()
progress =""
global progress1,tl2
s=0

def resume():
    mixer_music.unpause()
    pause_button=Button(text="pause",image=pause_icon,compound=TOP,font=("Times", ),command=res,width=60,).place(x=252,y=380)
    stop_buttun=Button(text="stop",image=stop_icon,compound=TOP,font=("Times"), width=60,command=stop).place(x=172,y=380)
     

def pay():
    mixer_music.unpause()
def res():
    mixer_music.pause()
    resume_button=Button(text="Resume",image=resume_icon,compound=TOP,font=("Times", ),command=resume,width=60,).place(x=252,y=380)
    play_buttun=Button(text="Play",image=play_icon,compound=TOP,font=("Times"), width=60,command=play).place(x=172,y=380)


    # pause_button=Button(text="resume",image=pause_icon,compound=TOP,font=("Times", ),command=res).place(x=232,y=380)
    # play_buttun=Button(text="Play",image=play_icon,compound=TOP,font=("Times", ),command=pay).place(x=232,y=380)
def stop():
    mixer_music.stop()
    play_buttun=Button(text="Play",image=play_icon,compound=TOP,font=("Times"), width=60,command=play).place(x=172,y=380)
    

def search():
    # global progress1
    au=filedialog.askopenfilename()
    a_t.set(au)
    
    if (a_t.get())=="":
        pass
       
    else:
        get=a_t.get()
        mixer_music.load(get)
        mixer_music.play()
        pause_button=Button(text="pause",image=pause_icon,compound=TOP,font=("Times", ),command=res,width=60).place(x=252,y=380)
        stop_buttun=Button(text="stop",image=stop_icon,compound=TOP,font=("Times"), width=60,command=stop).place(x=172,y=380)
        song=MP3(a_t.get())
        songl=int(song.info.length)
        print(songl)
        tl.configure(text=f'{datetime.timedelta(seconds=songl)}')

        progress1['maximum']=songl
        

        def hello():
            pos=mixer_music.get_pos()//1000
            
            # song=songl-pos
            # tl.configure(text=f'{int((song).timedelta(secconds=song))}')
            if pos!=songl:
                

                pp=datetime.timedelta(seconds=songl)
                progress1['value']=pos
                tl2.configure(text=f"{datetime.timedelta(seconds=pos)}")
                tl2.place(x=40,y=300)
            

                
            else:
                tl2.configure(text="00000")
                tl2.place(x=40,y=300)
            
            



            progress1.after(2,hello)
            
            
            # tl2.configure(text="0.0.0")
        


        
        hello()

# tl2.configure(text="0.0.0")
# progress1['value']=0.0
            
      


def play():

    mixer_music.load(a_t.get())
    mixer_music.play()

    pause_button=Button(text="pause",image=pause_icon,compound=TOP,font=("Times", ),command=res,width=60).place(x=252,y=380)
    stop_buttun=Button(text="stop",image=stop_icon,compound=TOP,font=("Times"), width=60,command=stop).place(x=172,y=380)
    song=MP3(a_t.get())
    songl=int(song.info.length)
    tl.configure(text=f'{datetime.timedelta(seconds=songl)}')

    print(songl)
    progress1['maximum']=songl
    def hello():
            pos=mixer_music.get_pos()//1000
            progress1['value']=pos
            tl2.configure(text=f'{datetime.timedelta(seconds=pos)}')
           
            progress1.after(2,hello)
    # tl2.configure(text="0.0.0")

    hello()
    # tl2.configure(text="0.0.0")

       

def v_up1():
    global progress,s
    v=mixer_music.get_volume()
    print(v)
    mixer_music.set_volume(v+0.1)
    p=mixer_music.get_volume()*100
    progress = Progressbar( orient = VERTICAL, 
              length = 250, mode = 'determinate',maximum=100,value=p) 
    progress.place(x=20,y=70)
    progress.update()

    progress = Progressbar( orient = VERTICAL, 
              length = 250, mode = 'determinate',maximum=100,value=p) 
    progress.place(x=480,y=70)
def nexts():
    p=[]
    for i in os.listdir(r'S:\ok'):
        p.append(f'S:\ok'+'\\'+i)
    f=random.choice(p)
    a_t.set(f)
    song=MP3(a_t.get())
    songl=int(song.info.length)
    print(songl)
    tl.configure(text=f'{datetime.timedelta(seconds=songl)}')

    progress1['maximum']=songl
    pause_button=Button(text="pause",image=pause_icon,compound=TOP,font=("Times", ),command=res,width=60).place(x=252,y=380)
    stop_buttun=Button(text="stop",image=stop_icon,compound=TOP,font=("Times"), width=60,command=stop).place(x=172,y=380)
    def hello():
            pos=mixer_music.get_pos()//1000
            progress1['value']=pos
            tl2.configure(text=f'{datetime.timedelta(seconds=pos)}')
           
            progress1.after(2,hello)
    # tl2.configure(text="0.0.0")

    hello()
    mixer_music.load(f)
    mixer_music.play()

    
def v_down1():
    # global s
    # # # s=0+1
    # global progress
    v=mixer_music.get_volume()
    print(v)
    mixer_music.set_volume(v-0.1)
    p=mixer_music.get_volume()*100
    progress = Progressbar( orient = VERTICAL, 
              length = 250, mode = 'determinate',maximum=100,value=p) 
    progress.place(x=20,y=70)
    progress.update()

    progress = Progressbar( orient = VERTICAL, 
              length = 250, mode = 'determinate',maximum=100,value=p) 
    progress.place(x=480,y=70)
    # p=[]
    # for i in os.listdir(r'S:\ok'):
    #     p.append(f'S:\ok'+'\\'+i)
    
    #     for item in range(1,5):
    #        mixer_music.load(p[s])
    #        mixer_music.play()
    # for i in os.listdir(r'S:\ok'):
    #     mixer_music.load(f'S:\ok'+'\\'+i)
    #     mixer_music.play()
    
    

        
          
    
    
    
    
    
    
    


    



root=Tk()
root.geometry("533x444")
root.resizable(0,0)
root.title("Suraj Music Player")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "—Pngtree—enjoying listening to music_5424708.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

logo2=Label(text="welcome to suraj Player",bg='yellow',fg='red',font=("Times", "24", "bold italic"))
logo2.place(x=120,y=10)

a_t=StringVar()
a_t.set(" S:/ok/hai mera dil1_(PagalWorld.com).mp3")
    

audio_track=ttk.Entry(root,textvariable=a_t,font=("Times", "24", "bold italic"),state='readonly',).place(x=100,y=330)
s_icon=PhotoImage(file='do.png')
play_icon=PhotoImage(file="d.png")
stop_icon=PhotoImage(file="stop.png")
pause_icon=PhotoImage(file="pause.png")
resume_icon=PhotoImage(file="images.png")
up_icon=PhotoImage(file="up.png")
down_icon=PhotoImage(file="down.png")
next_icon=PhotoImage(file="next.png")

s_button=Button(text="Search",image=s_icon,compound=TOP,font=("Times", ),command=search).place(x=20,y=340)
s1_button=Button(text="Search",image=s_icon,compound=TOP,font=("Times", ),command=search).place(x=437,y=340)
play_buttun=Button(text="Play",image=play_icon,compound=TOP,font=("Times"), width=60,command=play).place(x=172,y=380)
resume_button=Button(text="Resume",image=resume_icon,compound=TOP,font=("Times", ),command=res,width=60,).place(x=252,y=380)
up_buttun=Button( image=up_icon,compound=TOP,font=("Times", ),command=v_up1,).place(x=110,y=390)
down_buttun=Button( image=down_icon,compound=TOP,font=("Times", ),command=v_down1,).place(x=350,y=390)

progress1 = Progressbar( orient = HORIZONTAL, 
              length = 380, mode = 'determinate',maximum=100,value=0) 
progress1.place(x=70,y=300)

progress1.update()
next_buttun=Button(image=next_icon,command=nexts).place(x=400,y=250)
tl=Label(text="0.0.0")
tl.place(x=440,y=300)
tl2=Label(text="0.0.0")
tl2.place(x=40,y=300)

# tt=Text()
# tt.place(x=500,y=150)





root.mainloop()