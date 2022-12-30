from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep

def run(bg,font,e_bg,l_fg,e_se_bg):
    background=bg
    f=font
    entry_bg=e_bg
    label_fg=l_fg
    entry_select_bg=e_se_bg

    w=Tk()
    w.configure(bg='black')
    w.title('Welcome')
    w.iconbitmap('emp_welcome.ico')
    frame=Frame(w,bg=background)
    frame.pack(padx=5,pady=5,fill=BOTH)
    s=ttk.Style().configure('.',bordercolor='black',darkcolor='orange',background=background)
    l1=Label(frame,text='''Welcome to the Employee Database Management System
configuring software...''', font=f,bg=background,fg=label_fg)
    l1.pack(expand=True,fill=BOTH,pady=10,padx=10)
    progress=ttk.Progressbar(frame,length=200,mode='determinate', value=0,maximum=100,style=s)
    progress.pack(expand=True,fill=BOTH,pady=10,padx=10)
    i,k=0,4
    while i<=100:
        sleep(0.1)
        if i==20: sleep(0.8); k=2
        elif i==50: sleep(0.9); k=10
        progress['value']=i
        i+=k
        progress.update()
    sleep(0.5); w.destroy()
    return True
    
