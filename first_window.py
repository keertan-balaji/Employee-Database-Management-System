from tkinter import *
from tkinter import ttk
from time import sleep
import checking

#all important variables
l=False
j=''
key=False
def run(bg,font,e_bg,l_fg,e_se_bg,sql_username,sql_password):
    background=bg
    f=font
    entry_bg=e_bg
    label_fg=l_fg
    entry_select_bg=e_se_bg
    global sql_u,sql_p
    sql_u=sql_username
    sql_p=sql_password

    def val():
        global l,j,key
        username=u_entry.get()
        password=p_entry.get()
        flag=True
        if l!=True:
            j=Label(frame,text='',font=f,fg=label_fg,bg=background)
            j.grid(row=2,column=0)
        while flag==True:
            if checking.checking(username,password,sql_username,sql_password)==True:
                j.configure(text=''':) Logged in \n successfully :)''')
                j.update()
                sleep(2)
                flag=False
                w.quit()
                w.destroy()
            else: 
                j.config(text=''':( Unauthorised
Credentials.
Please
re-enter:''')
                j.update()
                l=True; break   
        
    w=Tk()
    w.configure(bg='black')
    w.title('Employee Database Management System')
    #w.geometry('570x280+50+50')
    
    w.iconbitmap('emp_login.ico')
    frame=Frame(w,bg=background)
    frame.pack(padx=5,pady=5)
    Grid.columnconfigure(frame,0,weight=1)
    Grid.rowconfigure(frame,0,weight=1)
    #labels
    u_label=Label(frame,text='Username:',font=f,fg=label_fg,bg=background,height=1)
    u_label.grid(row=0,column=0,ipadx=10,pady=10,sticky='nsew')
    p_label=Label(frame,text='Password:',font=f,fg=label_fg,bg=background,height=1)
    p_label.grid(row=1,column=0,ipadx=10,pady=10,sticky='nsew')

    # entries
    style=ttk.Style().configure('TEntry')
    
    u_entry=Entry(frame,background=entry_bg,
            relief='solid',bd=4,fg='black',
            selectbackground=entry_select_bg,
            font=f)
    u_entry.grid(row=0,column=1,ipadx=15,ipady=5,padx=10,pady=10,sticky='nsew')   
    u_entry.focus()
    u_entry.bind('<Return>',lambda e: p_entry.focus_set())

    p_entry=Entry(frame,background=entry_bg, relief='solid',bd=4,fg='black',
            selectbackground=entry_select_bg, font=f,show='*')
    p_entry.grid(row=1,column=1,ipadx=15,ipady=5,padx=10,pady=10,sticky='nsew')
    p_entry.bind('<Return>', lambda e: sign.focus_set())

    #buttons
    sign=Button(frame,text='Sign in',command=val,
                foreground='black',font=f,height=1,
                background='#FFC300',bd=4,highlightthickness=5,relief='solid')

            
    sign.grid(row=2,column=1,padx=30,pady=10,sticky='nsew')
    sign.bind('<Return>',lambda e:sign.invoke())
    sign.bind('<Up>',lambda e:p_entry.focus_set())
    u_entry.bind('<Down>',lambda e:p_entry.focus_set())
    p_entry.bind('<Up>',lambda e:u_entry.focus_set())
    p_entry.bind('<Down>',lambda e:sign.focus_set())
    
    
    op=True
    def close():
        global key
        if op: key=True; w.destroy()

    w.protocol('WM_DELETE_WINDOW',close)
    mainloop()
    return key
