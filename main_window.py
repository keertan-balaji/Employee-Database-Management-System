from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from time import sleep
import option1,option2,option3,option4,option5,option6,option7,option8,font_chooser,first_window
import connection_window,welcome_window,instructions
import mysql.connector
from tkinter import messagebox

sql_u='root' #username for sql
sql_p='root' #password for sql
new=None
mydb=mysql.connector.connect(host="localhost",user=sql_u,
                                 passwd=sql_p)
mycursor=mydb.cursor()
mycursor.execute('show databases')
gg=mycursor.fetchall()
if ('edms',) in gg:
    mycursor.execute("use edms")
    mycursor.execute("select * from preferences")
    cj=mycursor.fetchall()
    cj=cj[0]
    mycursor.execute('select * from instructions')
    ins=mycursor.fetchall()[0][0]
    print(cj)
    background=cj[0]
    f=eval(cj[1])
    entry_bg=cj[2]
    label_fg=cj[3]
    entry_select_bg=cj[4]
    b_bg=cj[5]
    b_fg=cj[6]
    rec()#to check if records are there or not when the program starts for the first time
    mycursor.close()
else:
    mycursor.close()
    background='#4F4B4B'
    f=("helvetica",20,'bold')
    entry_bg='#3498DB'
    label_fg='#FF8B00'
    entry_select_bg='orange'
    b_bg='#F6DC00'
    b_fg='black'
    ins='False'
jojo=None
        
def rec():
    global new
    db=mysql.connector.connect(host="localhost",user=sql_u,
                                 passwd=sql_p,database='edms')
    cursor=db.cursor()
    cursor.execute('select * from employee')
    jojo=cursor.fetchall()
    if jojo==[]:
        new=True
    else:
        new=False
    cursor.close()
t=['','Display an employee\'s details based on employee ID','Display all employee details',
          'Modify Records of employee',"Display employee's details based on their designation",
          'Display Employee\'s details based on their Salary',
          'Display an Employee\'s Salary Details','Delete Employee Records']
def empty():
    messagebox.showerror("Error",'''The database is empty please enter
a few records before displaying or modifying them :)''')
    

stats = [b_fg,b_bg,background,f,entry_bg,label_fg,entry_select_bg,sql_u,sql_p]
def opt1():
    option1.run(stats)
def opt2():
    rec()
    if new==False:
        option2.run(stats)
    else:
        empty()
def opt3():
    rec()
    if new==False:
        option3.run(stats)
    else:
        empty()
def opt4():
    rec()
    if new==False:
        option4.run(stats)
    else:
        empty()
def opt5():
    rec()
    if new==False:
        option5.run(stats)
    else:
        empty()
def opt6():
    rec()
    if new==False:
        option6.run(stats)
    else:
        empty()
def opt7():
    rec()
    if new==False:
        option7.run(stats)
    else:
        empty()
def opt8():
    rec()
    if new==False:
        option8.run(stats)
    else:
        empty()
def color(l):
    global background,f,entry_bg,label_fg,b_bg,b_fg,entry_select_bg
    bg=colorchooser.askcolor()
    j=bg[1]
    mydb=mysql.connector.connect(host="localhost",user=sql_u,
                                 passwd=sql_p,database="edms")
    mycursor=mydb.cursor()

    if bg!=(None,None):
        if l==1:background=j
        elif l==2:
            b_fg=j
            label_fg=j
        elif l==3:b_bg=j
        elif l==4:entry_bg=j
    mycursor.execute('delete from preferences')
    h='''insert into preferences(background,font,entry_background,label_foreground,
entry_select_background,button_background,button_foreground) values(%s,%s,%s,%s,%s,%s,%s)'''
    y=(background,str(f),entry_bg,label_fg,entry_select_bg,b_bg,b_fg)
    mycursor.execute(h,y)
    mydb.commit()
    mycursor.close()
    w.configure(background=background)
    w.update()
    for i in buttons:
        i.configure(bg=b_bg,activebackground=b_bg,foreground=b_fg)
        i.update()

def fontapp():
    global f,buttons
    mydb=mysql.connector.connect(host="localhost",user=sql_u,
                                 passwd=sql_p,database="edms")
    mycursor=mydb.cursor()

    f=font_chooser.run(button_color=b_bg,
                    bg=background,
                    font=f,
                    e_bg=entry_bg,
                    l_fg=label_fg,
                    e_se_bg=entry_select_bg,
                    sql_username=sql_u,
                    sql_password=sql_p)
    mycursor.execute('update preferences set font="{0}"'.format(f,))
    mydb.commit()
    mycursor.close()
    for i in buttons: i.configure(font=f); i.update()
def credit():
    top=Toplevel()
    top.geometry('500x200')
    top.iconbitmap('logo.ico')
    top.title('Credits')
    text=Text(top,font=f, selectbackground=entry_select_bg,
              wrap=WORD,padx=10,pady=2)
    text.insert(INSERT,'''This Employee database management system was
made by Abdul Amaan,Keertan Balaji and Aditya Ashmit Das.

Date of release:- 20/04/20

version:- 1.16.5
System Up to Date :)''')
    text.pack(expand=True)
    text.configure(state='disabled')
def default():
    global background,f,entry_bg,label_fg,b_bg,b_fg,entry_select_bg
    mydb=mysql.connector.connect(host="localhost",user=sql_u,
                                 passwd=sql_p,database="edms")
    mycursor=mydb.cursor()
    mycursor.execute('delete from preferences')
    mycursor.execute('''insert into preferences values('#4F4B4B',
            '("Helvetica",20,"bold")','#3498DB',
            '#FF8B00','orange','#F6DC00','black')''')
    mydb.commit()
    mycursor.close()
    background='#4F4B4B'
    f=("helvetica",20,'bold')
    entry_bg='#3498DB'
    label_fg='#FF8B00'
    entry_select_bg='orange'
    b_bg='#F6DC00'
    b_fg='black'
    w.configure(background=background)
    w.update()
    for i in buttons:
        i.configure(font=f)
        i.configure(bg=b_bg,activebackground=b_bg,foreground=b_fg)
        i.update()
def instruct(): instructions.run(stats, inst = False)
i=1

#invoking other modules
c1=first_window.run(background,f,entry_bg,
                  label_fg,
                  entry_select_bg,
                  sql_username=sql_u,
                  sql_password=sql_p)
if c1:
    quit
else:
    c2=connection_window.run(background,f,entry_bg,
                  label_fg,
                  entry_select_bg,
                sql_username=sql_u,sql_password=sql_p)
    c2=welcome_window.run(background,f,entry_bg,
                  label_fg,
                  entry_select_bg)
c1=False    

if c1!=True:
    if ins=='False': instructions.run(stats, inst = True)
    root=Tk()
    root.state('zoomed')
    root.title('Employee Database Management')
    root.attributes("-topmost",True)
    root.iconbitmap('logo.ico')
    root.attributes("-topmost",False)
    root.focus_force()

    container = ttk.Frame(root)
    canvas = Canvas(container)
    yscrollbar = ttk.Scrollbar(container,orient="vertical", command=canvas.yview)
    xscrollbar = ttk.Scrollbar(container,orient="horizontal", command=canvas.xview)
    w = Frame(canvas,background=background)
    w.pack()
    w.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    '''binds the canvas to the frame so that any change in the frame size and the scroll bars
attached also change with it'''
    canvas.create_window((0, 0), window=w, anchor="nw")

    container.pack(fill=BOTH,expand=True)
    xscrollbar.pack(side="bottom", fill="x")
    yscrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=yscrollbar.set)
    canvas.configure(xscrollcommand=xscrollbar.set)
    canvas.pack(fill="both",expand=True)

    buttons=[]
    frames=[]

    for i in range(9):
        frr=LabelFrame(w,width=370,height=160,background='white',highlightthickness=2,
                       bd=2,relief='solid',highlightcolor='blue')
        b=Button(frr,bd=4,
                 height=5,
                 background=b_bg,relief='solid',fg=b_fg,font=f,
                 activebackground=b_bg,wraplength=290,
                 highlightcolor='blue')
        b.grid(row=0,sticky='nsew')
        buttons.append(b)
        frames.append(frr)
        Grid.columnconfigure(frr,0,weight=1)
        Grid.rowconfigure(frr,0,weight=1)
        frr.grid_propagate(False)

    r=c=0
    for i in frames:
        if r==3: r=0; c+=1
        i.grid(row=r,column=c,padx=45,pady=40)
        r+=1
    
    menu=Menu(root)
    root.configure(menu=menu)

    submenus=[]

    p=Menu(menu,tearoff=0)
    p.add_command(label='Customise background colour',command= lambda:color(1))
    p.add_command(label='Customise font',command=fontapp)
    p.add_command(label='Customise font colour',command=lambda:color(2))
    p.add_command(label='Customise button colour',command=lambda:color(3))
    p.add_command(label='Customise entry box colour',command=lambda:color(4))
    p.add_command(label='Restore Defaults settings',command=default)

    h=Menu(menu,tearoff=0)
    h.add_command(label='About us',command=credit)
    h.add_command(label='Instructions',command=instruct)
    
    menu.add_cascade(label='Personalization',menu=p)
    menu.add_cascade(label='Help',menu=h)
        
    buttons[0].configure(text='Enter employee details', command=opt1)
    buttons[0].focus()
    buttons[0].bind('<Down>',lambda a:buttons[1].focus_set())
    buttons[0].bind('<Right>',lambda a:buttons[3].focus_set())

    buttons[1].bind('<Down>',lambda a:buttons[2].focus_set())
    buttons[1].bind('<Right>',lambda a:buttons[4].focus_set())
    buttons[1].bind('<Up>',lambda a:buttons[0].focus_set())

    buttons[2].bind('<Up>',lambda a:buttons[1].focus_set())
    buttons[2].bind('<Right>',lambda a:buttons[5].focus_set())

    buttons[3].bind('<Down>',lambda a:buttons[4].focus_set())
    buttons[3].bind('<Right>',lambda a:buttons[6].focus_set())
    buttons[3].bind('<Left>',lambda a:buttons[0].focus_set())

    buttons[4].bind('<Down>',lambda a:buttons[5].focus_set())
    buttons[4].bind('<Right>',lambda a:buttons[7].focus_set())
    buttons[4].bind('<Up>',lambda a:buttons[3].focus_set())
    buttons[4].bind('<Left>',lambda a:buttons[1].focus_set())

    buttons[5].bind('<Left>',lambda a:buttons[2].focus_set())
    buttons[5].bind('<Right>',lambda a:buttons[8].focus_set())
    buttons[5].bind('<Up>',lambda a:buttons[4].focus_set())

    buttons[6].bind('<Down>',lambda a:buttons[7].focus_set())
    buttons[6].bind('<Left>',lambda a:buttons[3].focus_set())

    buttons[7].bind('<Up>',lambda a:buttons[6].focus_set())
    buttons[7].bind('<Down>',lambda a:buttons[8].focus_set())
    buttons[7].bind('<Left>',lambda a:buttons[4].focus_set())

    buttons[8].bind('<Up>',lambda a:buttons[7].focus_set())
    buttons[8].bind('<Left>',lambda a:buttons[5].focus_set())

    buttons[0].configure(text='Enter employee details into database', command=opt1)
    buttons[1].configure(text=t[1],command=opt2)
    buttons[2].configure(text=t[2],command=opt3)
    buttons[3].configure(text=t[3],command=opt4)
    buttons[4].configure(text=t[4],command=opt5)
    buttons[5].configure(text=t[5],command=opt6)
    buttons[6].configure(text=t[6],command=opt7)
    buttons[7].configure(text=t[7],command=opt8)
    buttons[8].configure(command=root.destroy,text='Exit')

    buttons[0].bind('<Return>',lambda a:buttons[0].invoke())
    buttons[1].bind('<Return>',lambda a:buttons[1].invoke())
    buttons[2].bind('<Return>',lambda a:buttons[2].invoke())
    buttons[3].bind('<Return>',lambda a:buttons[3].invoke())
    buttons[4].bind('<Return>',lambda a:buttons[4].invoke())
    buttons[5].bind('<Return>',lambda a:buttons[5].invoke())
    buttons[6].bind('<Return>',lambda a:buttons[6].invoke())
    buttons[7].bind('<Return>',lambda a:buttons[7].invoke())
    buttons[8].bind('<Return>',lambda a:buttons[8].invoke())
    
    mainloop()
