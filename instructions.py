from tkinter import *
from tkinter import ttk
import mysql.connector

def run(stats,inst):
    b_fg=stats[0]
    b_bg=stats[1]
    background=stats[2]
    f=list(stats[3])
    #print(f)
    f[1]=18
    f=tuple(f)
    entry_bg=stats[4]
    label_fg=stats[5]
    entry_select_bg=stats[6]
    sql_u=stats[7]
    sql_p=stats[8]
    
    def a():
        db=mysql.connector.connect(host = "localhost", database = 'edms',
                                    user = sql_u, password = sql_p)
        cursor=db.cursor()
        cursor.execute("delete from instructions")
        cursor.execute("insert into instructions values('True')")
        db.commit()
        cursor.close()

    w=Tk()
    w.configure(bg ='black')
    w.title("Instructions")
    w.iconbitmap('logo.ico')
    w.focus_force()
    frame=Frame(w)
    t=Text(frame,width=30,height=10,relief='solid',bd=3,
           selectbackground='orange',font=('',16,'bold'),
           wrap=WORD,padx=10,pady=2,fg='black')
    t.insert(INSERT,'''INSTRUCTIONS:-
1) WHILE ENTERING DATE ANYWHERE IN THE APPLICATION PLEASE FOLLOW THE YYYY-MM-DD AND TYPE THE HYPHEN AS WELL

2) DO NOT ENTER ALPHABETS OR OTHER CHARACTER WHEN INPUTING DATA LIKE SALARY,EARNED LEAVE ETC. IT WILL NOT WORK''')

    yscroll_bar=ttk.Scrollbar(frame,orient='vertical',command=t.yview)
    t.configure(yscrollcommand=yscroll_bar.set)
    yscroll_bar.pack(side=RIGHT,fill=Y)
    style=ttk.Style()
    style.configure('TCheckbutton',bg=background,relief='solid')
    c=ttk.Checkbutton(frame,text='Dont show this again',
                  onvalue=1,offvalue=0,command=a)
    t.pack(fill=BOTH,expand=True)
    if inst:
        c.pack(expand=True)
        t.insert(INSERT,'''\n\n3)YOUR DATABASE WILL BE EMPTY I.E THERE WILL BE NO RECORDS PRESENT YOU WILL HAVE TO INSERT THE RECORDS WHICH U CAN DO BY SELECTING THE ENTER EMPLOYEE DETAILS OPTIONS.''')
    frame.pack(padx=4,pady=4,expand=True)
    t.configure(state='disabled')
    
    mainloop()

