from tkinter import ttk
from tkinter import *
root=Tk()
root.title("Unit conversion")
root.geometry("400x400")
root.config(bg="#E0FFFF")
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
    
    if combos1=="METER" and combos2=="KILOMETER":
        texts=float(entrys1)/1000
    elif combos1=="KILOMETER" and combos2=="METER":
        texts=float(entrys1)*1000
    elif combos1=="CENTIMETER" and combos2=="METER":
        texts=float(entrys1)/100
    elif combos1=="METER" and combos2=="CENTIMETER":
        texts=float(entrys1)*100
    elif combos1=="KILOMETER" and combos2=="CENTIMETER":
        texts=float(entrys1)*100000
    elif combos1=="CENTIMETER" and combos2=="KILOMETER":
        texts=float(entrys1)/100000
    elif combos1=="MILIMETER" and combos2=="METER":
        texts=float(entrys1)/1000
    elif combos1=="METER" and combos2=="MILIMETER":
        texts=float(entrys1)*1000
    elif combos1=="MILIMETER" and combos2=="KILOMETER":
        texts=float(entrys1)/1000000
    elif combos1=="KILOMETER" and combos2=="MILIMETER":
        texts=float(entrys1)*1000000
    elif combos1=="MILIMETER" and combos2=="CENTIMETER":
        texts=float(entrys1)/10
    elif combos1=="CENTIMETER" and combos2=="MILIMETER":
        texts=float(entrys1)*10
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
lbl1=Label(root, text="FROM",bg="#E0FFFF")
lbl1.pack()
combo1= ttk.Combobox(root,state= "readonly")
combo1['values']=("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo1.current()
combo1.bind("<<ComboboxSelected>>", get)
combo1.pack()
lbl2=Label(root, text="To", bg="#E0FFFF")
lbl2.pack()
combo2= ttk.Combobox(root,state= "readonly")
combo2['values']=("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo2.current()
combo2.bind("<<ComboboxSelected>>", get)
combo2.pack()
entry1=Entry(root)
entry1.pack()
btn=Button(root,command=tabdil,text="CONVERT", height=2, width=12, bg="#FFC0CB")
btn.pack()
lbl=Label(root, bg="#E0FFFF", font="bold")
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
    
    if combos3=="METER" and combos4=="KILOMETER":
        texts1=float(entrys2)/1000
    elif combos3=="KILOMETER" and combos4=="METER":
        texts1=float(entrys2)*1000
    elif combos3=="CENTIMETER" and combos4=="METER":
        texts1=float(entrys2)/100
    elif combos3=="METER" and combos4=="CENTIMETER":
        texts1=float(entrys2)*100
    elif combos3=="KILOMETER" and combos4=="CENTIMETER":
        texts1=float(entrys2)*100000
    elif combos3=="CENTIMETER" and combos4=="KILOMETER":
        texts1=float(entrys2)/100000
    elif combos3=="MILIMETER" and combos4=="METER":
        texts1=float(entrys2)/1000
    elif combos3=="METER" and combos4=="MILIMETER":
        texts1=float(entrys2)*1000
    elif combos3=="MILIMETER" and combos4=="KILOMETER":
        texts1=float(entrys2)/1000000
    elif combos3=="KILOMETER" and combos4=="MILIMETER":
        texts1=float(entrys2)*1000000
    elif combos3=="MILIMETER" and combos4=="CENTIMETER":
        texts1=float(entrys2)/10
    elif combos3=="CENTIMETER" and combos4=="MILIMETER":
        texts1=float(entrys2)*10
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
lbl5=Label(root, text="FROM",bg="#E0FFFF")
lbl5.pack()
combo3= ttk.Combobox(root,state= "readonly")
combo3['values']=("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo3.current()
combo3.bind("<<ComboboxSelected>>", getnew)
combo3.pack()
lbl4=Label(root, text="To", bg="#E0FFFF")
lbl4.pack()
combo4= ttk.Combobox(root,state= "readonly")
combo4['values']=("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo4.current()
combo4.bind("<<ComboboxSelected>>", getnew)
combo4.pack()
entry2=Entry(root)
entry2.pack()
btn1=Button(root,command=tabdilnew,text="CONVERT", height=2, width=12, bg="#FFC0CB")
btn1.pack()
lbl14=Label(root, bg="#E0FFFF", font="bold")
lbl14.pack()
root.mainloop()