from tkinter import ttk
from tkinter import *
root=Tk()
root.title("Currency conversion")
root.geometry("400x400")
root.config(bg="#FFFF00")
# root.resizable(False,False)
combos1=""
combos2=""
#combos3=""
#combos4=""
entrys1=""
# entrys2=""
def checkValue(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
    
def tabdil():
    global combos2
    global combos1
    global entrys1
    global texts
    texts=""
    entrys1=entry1.get()

    if entrys1=='':
        return
    
    if(checkValue(entrys1)==False):
        lbl.config(text="Not a number!")
        return
    
    if combos1=="TOMAN" and combos2=="POUND":
        texts=float(entrys1)/80000
    elif combos1=="POUND" and combos2=="TOMAN":
        texts=float(entrys1)*80000
    elif combos1=="DOLLAR" and combos2=="TOMAN":
        texts=float(entrys1)*61000
    elif combos1=="TOMAN" and combos2=="DOLLAR":
        texts=float(entrys1)/61000
    elif combos1=="POUND" and combos2=="DOLLAR":
        texts=float(entrys1)*1.2
    elif combos1=="DOLLAR" and combos2=="POUND":
        texts=float(entrys1)/1.2
    elif combos1=="EURO" and combos2=="TOMAN":
        texts=float(entrys1)*68150
    elif combos1=="TOMAN" and combos2=="EURO":
        texts=float(entrys1)/68150
    elif combos1=="EURO" and combos2=="POUND":
        texts=float(entrys1)*0.834
    elif combos1=="POUND" and combos2=="EURO":
        texts=float(entrys1)/0.834
    elif combos1=="EURO" and combos2=="DOLLAR":
        texts=float(entrys1)*1.16
    elif combos1=="DOLLAR" and combos2=="EURO":
        texts=float(entrys1)*0.896
    elif combos1==combos2:
        texts=entrys1
    # texts=f'{texts:.5f}'
    lbl.config(text=texts)
    # if entrys2=='':
    #     return
    #combos3==""
        
    
def get(event):
    global combos1
    global combos2
    # global #combos4
    # global #combos3
    combos1=combo1.get()
    combos2=combo2.get()
    # tabdil()
    #combos3=combo3.get()
    #combos4=combo4.get()
lbl1=Label(root, text="FROM",bg="#FFFF00")
lbl1.pack()
combo1= ttk.Combobox(root,state= "readonly")
combo1['values']=("TOMAN", "POUND", "DOLLAR", "EURO")
combo1.current()
combo1.bind("<<ComboboxSelected>>", get)
combo1.pack()
lbl2=Label(root, text="To", bg="#FFFF00")
lbl2.pack()
combo2= ttk.Combobox(root,state= "readonly")
combo2['values']=("TOMAN", "POUND", "DOLLAR", "EURO")
combo2.current()
combo2.bind("<<ComboboxSelected>>", get)
combo2.pack()
entry1=Entry(root)
entry1.pack()
btn=Button(root,command=tabdil,text="CONVERT", height=2, width=12, bg="#ADFF2F")
btn.pack()
lbl=Label(root, bg="#FFFF00", font="bold")
lbl.pack()
combos3=""
combos4=""
#combos3=""
#combos4=""
entrys2=""
# entrys2=""
def checkValuenew(vala):
    try:
        float(vala)
        return True
    except ValueError:
        return False
    
def tabdilnew():
    global combos3
    global combos4
    global entrys2
    global texts1
    texts1=""
    entrys2=entry2.get()

    if entrys2=='':
        return
    
    if(checkValuenew(entrys2)==False):
        lbl14.config(text="Not a number!")
        return
    
    if combos3=="TOMAN" and combos4=="POUND":
        texts1=float(entrys2)/80000
    elif combos3=="POUND" and combos4=="TOMAN":
        texts1=float(entrys2)*80000
    elif combos3=="DOLLAR" and combos4=="TOMAN":
        texts1=float(entrys2)*61000
    elif combos3=="TOMAN" and combos4=="DOLLAR":
        texts1=float(entrys2)/61000
    elif combos3=="POUND" and combos4=="DOLLAR":
        texts1=float(entrys2)*1.2
    elif combos3=="DOLLAR" and combos4=="POUND":
        texts1=float(entrys2)/1.2
    elif combos3=="EURO" and combos4=="TOMAN":
        texts1=float(entrys2)*68150
    elif combos3=="TOMAN" and combos4=="EURO":
        texts1=float(entrys2)/68150
    elif combos3=="EURO" and combos4=="POUND":
        texts1=float(entrys2)*0.834
    elif combos3=="POUND" and combos4=="EURO":
        texts1=float(entrys2)/0.834
    elif combos3=="EURO" and combos4=="DOLLAR":
        texts1=float(entrys2)*1.16
    elif combos3=="DOLLAR" and combos4=="EURO":
        texts1=float(entrys2)*0.896
    elif combos3==combos4:
        texts1=entrys2
    # texts1=f'{texts1:.5f}'
    lbl14.config(text=texts1)
    # if entrys2=='':
    #     return
    #combos3==""
        
    
def getnew(event):
    global combos3
    global combos4
    # global #combos4
    # global #combos3
    combos3=combo3.get()
    combos4=combo4.get()
    # tabdil()
    #combos3=combo3.get()
    #combos4=combo4.get()
lbl5=Label(root, text="FROM",bg="#FFFF00")
lbl5.pack()
combo3= ttk.Combobox(root,state= "readonly")
combo3['values']=("TOMAN", "POUND", "DOLLAR", "EURO")
combo3.current()
combo3.bind("<<ComboboxSelected>>", getnew)
combo3.pack()
lbl4=Label(root, text="To", bg="#FFFF00")
lbl4.pack()
combo4= ttk.Combobox(root,state= "readonly")
combo4['values']=("TOMAN", "POUND", "DOLLAR", "EURO")
combo4.current()
combo4.bind("<<ComboboxSelected>>", getnew)
combo4.pack()
entry2=Entry(root)
entry2.pack()
btn1=Button(root,command=tabdilnew,text="CONVERT", height=2, width=12, bg="#ADFF2F")
btn1.pack()
lbl14=Label(root, bg="#FFFF00", font="bold")
lbl14.pack()
root.mainloop()