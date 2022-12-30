from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep
import mysql.connector
key=False
def run(bg,font,e_bg,l_fg,e_se_bg,sql_username,sql_password):
    background=bg
    f=font
    entry_bg=e_bg
    label_fg=l_fg
    entry_select_bg=e_se_bg 
    sql_u=sql_username
    sql_p=sql_password

    def check():
        mydb=mysql.connector.connect(host='localhost',user=sql_u,
                                    password=sql_p)
        mycursor=mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        if ('edms',) in mycursor: return True
        else: return False   

    global l1,b1,key
    w=Tk()
    w.configure(bg=background)
    w.title('Connection Establishment')
    w.iconbitmap('emp_connect.ico')
    
    if key==False:
        if check()==False:
            l1=Label(w,text='''Please wait while we
create the Database......''',font=f,bg=background,fg=label_fg)
            l1.grid(row=0)
            s=ttk.Style().configure('TProgressbar',
                bordercolor='black',darkcolor='orange',background=background)
            progress=ttk.Progressbar(w,length=200,
                                         mode='determinate',
                                         value=0,maximum=100,
                                     style=s)
            progress.grid(row=1)
            i,k=0,4
            mydb=mysql.connector.connect(host='localhost',user=sql_u,password=sql_p)
            mycursor=mydb.cursor()
            mycursor.execute("CREATE DATABASE edms")
            while i<=100:
                if i==1: sleep(1)
                sleep(0.1)
                progress['value']=i
                i+=k
                progress.update()
            sleep(0.5)
            progress.grid_forget()
            l1.configure(text='Database created successfully')
            l1.update()
            sleep(1.5)
            mydb=mysql.connector.connect(host="localhost",user="root",
                                         passwd="root",database="edms")
            mycursor=mydb.cursor()
            mycursor.execute('''create table employee(
                                emp_id int not null primary key,
                                name varchar(255),
                                DOB date,
                                address varchar(255),
                                bank_ac decimal(26) ,
                                pan_no varchar(10),
                                designation varchar(255),
                                department varchar(255),
                                reporting_manager varchar(255),
                                el int,
                                pl int,
                                salary double,
                                netpay double,
                                itax double,
                                bonus double)''')
            mycursor.execute('''create table security(username varchar(255),
password varchar(300))''')
            mycursor.execute('insert into security values("root","R31!")')
            mycursor.execute('insert into security values("1","1#$1")')
            mycursor.execute('''create table preferences(
                                background varchar(12),
                                font varchar(100),
                                entry_background varchar(12),
                                label_foreground varchar(12),
                                entry_select_background varchar(12),
                                button_background varchar(12),
                                button_foreground varchar(12))''')
            mycursor.execute('''create table instructions(value varchar(6))''')
            mycursor.execute('''INSERT INTO instructions VALUES('False')''')
            mycursor.execute('''INSERT INTO preferences VALUES('#4F4B4B',
            '("Helvetica",20,"bold")','#3498DB',
            '#FF8B00','orange','#F6DC00','black')''')
            key=True
            mydb.commit()
            mycursor.close()

        else:
            l1=Label(w,text='''Connected to the Database
Successfully''',font=f,bg=background,fg=label_fg)
            l1.grid(row=0)
            l1.update()
            sleep(1)
            key=True
    
    if key==True: w.destroy()
    else: mainloop()
    return key
