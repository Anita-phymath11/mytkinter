#this is an app which makes a random password in range of the input characters
from tkinter import *
from tkinter import ttk
from random import randint as r
from random import choice as c
root=Tk()
root.geometry("700x350")
root.title("MAKE A RANDOM PASSWORD")
lpass=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v","w", "x","y", "z","0","1","2","3","4","5","6","7","8","9","10","!","@","#","$","%","^","&","*","(",")","_","-","=","+","|","}","{","[","]",";",":",".","<",">",",","?","/","~","`"]
#lpass is the list of the characters which randomly make a password
mychoice=""
root.config(bg="#DC143C")
def game():
    #this function gets the entry and makes a random password in the range of it and if the entry was empty, doesn't work
    global texts
    texts=""
    entrys=entry.get()
    if entrys=="":
        texts="ERROR! NO INPUT"
        lbl.config(text=texts)
        return
    for i in range (int(entrys)):
        print("hi")
        texts+=c(lpass)
    lbl.config(text=texts)
# def addclick():
#     inputValue=entry.get()
#     print(inputValue)
#     if(inputValue!=""):
#         listbox.insert(END, inputValue)
#         entry.delete(0,END)
def add():
    if texts!="":
        listbox.insert(END,texts)
        entry.delete(0,END)
def deleteclick():
    index=listbox.curselection()         
    if index!=():
        listbox.delete(index)
#entry 
lb=Label(root,text="ENTER A NUMBER A CREAT A RANDOM PSSWORD", bg="#AFEEEE")
lb.pack()
entry=Entry(root, width=50)
entry.pack()
var=StringVar
lbl=Label(root, bg="#DC143C", fg="#AFEEEE", font="bold")
lbl.pack()
listbox=Listbox(root, width=98)
listbox.pack()
#(fill=BOTH, expand=True)
btn=Button(root,command=game,text="confirm", height=2, width=12, bg="#AFEEEE")
btn.pack()
btn1=Button(root,command=add,text="add to the list", height=2, width=12, bg="#AFEEEE")
btn1.pack()





























root.mainloop()