from tkinter import *
from tkinter import ttk
from tkinter import font
global key
key=False

def run(button_color,bg,font,e_bg,l_fg,e_se_bg,
        sql_username,sql_password):
    background=bg
    entry_bg=e_bg
    label_fg=l_fg
    entry_select_bg=e_se_bg
    b_bg=button_color
    sql_u=sql_username
    sql_p=sql_password

    f=['Arial',20,'bold']

    #while key==False:  
    def setting_font(val):
        global key
        r1=k.get(); r2=g.get()
        if (r1 in fonts) and (r2 in t): f[0]=r1; f[2]=r2
        if val==1: key=True; w.quit(); w.destroy()
        else:
            textbox.configure(font=f)
            textbox.update()
        
    w=Tk()
    w.configure(bg='black')
    w.title('Font selection Dialog Box')
    w.iconbitmap('logo.ico')
    frame=Frame(w,bg=background)
    frame.pack(pady=5,padx=5,fill=BOTH)
    l1=Label(frame,text='Font',font=f,bg=background,fg=label_fg)
    l2=Label(frame,text='Font Style',font=f,bg=background,fg=label_fg)

    textbox=Text(frame,width=20,height=4,relief='solid',bd=3,
                 selectbackground='orange',font=f,wrap=WORD,padx=10,pady=2)
    textbox.insert(INSERT,'The Fox jumps over the Fence')

    fonts=['Algerian','Arial','Arial Rounded MT',
           'Baskerville Old Face','Bauhaus 93',
           'Bernard MT','Bookman Old Style',
           'Bradley Hand ITC','Britannic',
           'Brush Script MT','Calibri','Chiller',
           'Comic Sans MS','Cooper','Curlz MT',
           'Forte','Franklin Gothic',
           'Freestyle Script','Gabriola',
           'Harlow Solid','Harrington',
           'Ink Free','Kristen ITC']

    t=['normal','bold','italic','roman','underline']

    style=ttk.Style().configure('TCombobox',font=f,bg='red')

    frr1=Frame(frame,bg='black')
    frr2=Frame(frame,bg='black')
    k=ttk.Combobox(frr1,style='TCombobox')
    g=ttk.Combobox(frr2,style=style)
    k.pack(fill=BOTH,expand=True,padx=4,pady=4)
    g.pack(fill=BOTH,expand=True,padx=4,pady=4)
    g.set('Select Style')
    k.set('Select Font')
    g['values']=t

    k['values']=fonts

    b1=Button(frame,text='Preview',relief='solid',
              bd=3,font=f,bg=b_bg,fg=label_fg,command=lambda:setting_font(0))
    b2=Button(frame,text='Apply',
              relief='solid',bd=3,font=f,
              bg=b_bg,fg=label_fg,command=lambda:setting_font(1))
    
    l1.grid(row=0,padx=10,sticky=N+S+E+W)
    l2.grid(row=0,column=1,padx=10,sticky=N+S+E+W)
    frr1.grid(row=1,padx=10,pady=10,sticky=N+S+E+W)
    frr2.grid(row=1,column=1,padx=10,pady=10,sticky=N+S+E+W)
    textbox.grid(row=2,padx=10,pady=10,rowspan=2,sticky=N+S+E+W)
    b1.grid(row=2,column=1,sticky=N+S+E+W,padx=10,pady=10)
    b2.grid(row=3,column=1,sticky=N+S+E+W,padx=10,pady=10)
    Grid.columnconfigure(frame,0,weight=1)
    Grid.rowconfigure(frame,0,weight=1)

    w.mainloop()
    return f
