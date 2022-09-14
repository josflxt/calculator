from tkinter import *

root=Tk()
root.title("JOEL CALCULATOR")

e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def butt
    if math=="addition":
        e.insert(0,fnumb+int(snumb))
    if math=="subtractio":
        e.insert(0,fnumb-int(snumb))
    if math=="multiplication":
        e.insert(0,fnumb*int(snumb))
    if math=="division":
        e.insert(0,fnumb/int(snumb))
    

    
def buttonadd():
    numb=e.get()
    global fnumb
    global math
    math="addition"
    fnumb=int(numb)
    e.delete(0,END)

def buttonsub():
    numb=e.get()
    global fnumb
    global math
    math="subtraction"
    fnumb=int(numb)
    e.delete(0,END)

def buttonmulti():
    numb=e.get()
    global fnumb
    global math
    math="multiplication"
    fnumb=int(numb)
    e.delete(0,END)
def buttondiv():
    numb=e.get()
    global fnumb
    global math
    math="division"
    
    fnumb=int(numb)
    e.delete(0,END)

number1=Button(root,text="1",padx=40,pady=20,command=lambda: buttonclick(1))
numbe
number1.grid(row=3,column=0)
number2.grid(row=3,column=1)
number3.grid(row=3,column=2)

number4.grid(row=2,column=0)
number5.grid(row=2,column=1)
number6.grid(row=2,column=2)

number7.grid(row=1,column=0)
number8.grid(row=1,column=1)
number9.grid(row=1,column=2)

number0.grid(row=4,column=1)mnspan=2)
numberclear.grid(row=5,column=1,columnspan=2)

numbersub.grid(row=4,column=2)
numbermulti.grid(row=5,column=0)
numberdiv.grid(row=6,column=0)


root.mainloop()


