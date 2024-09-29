from tkinter import ttk
from tkinter import *
root=Tk()
root.title("Temperature conversion")
root.geometry("400x400")
root.config(bg="#FFE4B5")
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
    
    if combos1=="CELSIUS" and combos2=="FAHRENHEIT":
        texts=float(entrys1)*1.8+32
    elif combos1=="FAHRENHEIT" and combos2=="CELSIUS":
        texts=float(entrys1)-32/1.8
    elif combos1=="CELVIN" and combos2=="CELSIUS":
        texts=float(entrys1)-273.15
    elif combos1=="CELSIUS" and combos2=="CELVIN":
        texts=float(entrys1)+273.15
    elif combos1=="FAHRENHEIT" and combos2=="CELVIN":
        texts=float(entrys1)+ 459.67/1.8
    elif combos1=="CELVIN" and combos2=="FAHRENHEIT":
        texts=float(entrys1) *1.8-459.67
    elif combos1=="RANKIN" and combos2=="CELSIUS":
        texts=float(entrys1)-32-459.67/1.8
    elif combos1=="CELSIUS" and combos2=="RANKIN":
        texts=float(entrys1)*1.8+32+459.67
    elif combos1=="RANKIN" and combos2=="FAHRENHEIT":
        texts=float(entrys1)-459.67
    elif combos1=="FAHRENHEIT" and combos2=="RANKIN":
        texts=float(entrys1)+459.67
    elif combos1=="RANKIN" and combos2=="CELVIN":
        texts=float(entrys1)/1.8
    elif combos1=="CELVIN" and combos2=="RANKIN":
        texts=float(entrys1)*1.8
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
lbl1=Label(root, text="FROM",bg="#FFE4B5")
lbl1.pack()
combo1= ttk.Combobox(root,state= "readonly")
combo1['values']=("CELSIUS", "FAHRENHEIT", "CELVIN", "RANKIN")
combo1.current()
combo1.bind("<<ComboboxSelected>>", get)
combo1.pack()
lbl2=Label(root, text="To", bg="#FFE4B5")
lbl2.pack()
combo2= ttk.Combobox(root,state= "readonly")
combo2['values']=("CELSIUS", "FAHRENHEIT", "CELVIN", "RANKIN")
combo2.current()
combo2.bind("<<ComboboxSelected>>", get)
combo2.pack()
entry1=Entry(root)
entry1.pack()
btn=Button(root,command=tabdil,text="CONVERT", height=2, width=12, bg="#FFA500")
btn.pack()
lbl=Label(root, bg="#FFE4B5", font="bold")
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
    
    if combos3=="CELSIUS" and combos4=="FAHRENHEIT":
        texts1=float(entrys2)*1.8+32
    elif combos3=="FAHRENHEIT" and combos4=="CELSIUS":
        texts1=float(entrys2)-32/1.8
    elif combos3=="CELVIN" and combos4=="CELSIUS":
        texts1=float(entrys2)-273.15
    elif combos3=="CELSIUS" and combos4=="CELVIN":
        texts1=float(entrys2)+273.15
    elif combos3=="FAHRENHEIT" and combos4=="CELVIN":
        texts1=float(entrys2)+ 459.67/1.8
    elif combos3=="CELVIN" and combos4=="FAHRENHEIT":
        texts1=float(entrys2) *1.8-459.67
    elif combos3=="RANKIN" and combos4=="CELSIUS":
        texts1=float(entrys2)-32-459.67/1.8
    elif combos3=="CELSIUS" and combos4=="RANKIN":
        texts1=float(entrys2)*1.8+32+459.67
    elif combos3=="RANKIN" and combos4=="FAHRENHEIT":
        texts1=float(entrys2)-459.67
    elif combos3=="FAHRENHEIT" and combos4=="RANKIN":
        texts1=float(entrys2)+459.67
    elif combos3=="RANKIN" and combos4=="CELVIN":
        texts1=float(entrys2)/1.8
    elif combos3=="CELVIN" and combos4=="RANKIN":
        texts1=float(entrys2)*1.8
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
lbl5=Label(root, text="FROM",bg="#FFE4B5")
lbl5.pack()
combo3= ttk.Combobox(root,state= "readonly")
combo3['values']=("CELSIUS", "FAHRENHEIT", "CELVIN", "RANKIN")
combo3.current()
combo3.bind("<<ComboboxSelected>>", getnew)
combo3.pack()
lbl4=Label(root, text="To", bg="#FFE4B5")
lbl4.pack()
combo4= ttk.Combobox(root,state= "readonly")
combo4['values']=("CELSIUS", "FAHRENHEIT", "CELVIN", "RANKIN")
combo4.current()
combo4.bind("<<ComboboxSelected>>", getnew)
combo4.pack()
entry2=Entry(root)
entry2.pack()
btn1=Button(root,command=tabdilnew,text="CONVERT", height=2, width=12, bg="#FFA500")
btn1.pack()
lbl14=Label(root, bg="#FFE4B5", font="bold")
lbl14.pack()
root.mainloop()