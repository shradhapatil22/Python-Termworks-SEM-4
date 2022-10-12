import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("600x400")
#ADD FRAME
frame=ttk.Frame(root,padding="10 10 10 10")
frame.pack()
# ADD WIDGETS
ttk.Label(frame,text="First number: ").grid(row=0,column=0,sticky=tk.E)
first=tk.StringVar()
ttk.Entry(frame,width=15,textvariable=first).grid(row=0,column=1)

ttk.Label(frame,text="Second number: ").grid(row=1,column=0,sticky=tk.E)
second=tk.StringVar()
ttk.Entry(frame,width=15,textvariable=second).grid(row=1,column=1)
def add():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo + secondNo)

def sub():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo - secondNo)

def mul():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo * secondNo)

def div():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo / secondNo)

ttk.Button(frame,text="Add ",command=add).grid(row=2,column=0)
ttk.Button(frame,text="Sub ",command=sub).grid(row=2,column=1)
ttk.Button(frame,text="Mul ",command=mul).grid(row=2,column=2)
ttk.Button(frame,text="Div ",command=div).grid(row=2,column=3)

ttk.Label(frame,text="Result: " ).grid(row=3,column=0,sticky=tk.E)
result=tk.StringVar()
ttk.Entry(frame,width=15,textvariable=result,state="readonly").grid(row=3,column=1)

for child in frame.winfo_children():
    child.grid_configure(padx=10,pady=10)

root.mainloop()