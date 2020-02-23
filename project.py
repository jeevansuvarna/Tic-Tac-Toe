
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Welcome")
window.geometry("1370x780")
window.configure(bg="mediumpurple3")
f1=Frame(window,borderwidth=9,relief='raised',bg="red3")
f1.grid(row=0,column=5,columnspan=11)
l1=Label(f1,text="*TIC-TAC-TOE*",font=("Comic Sans MS",'40'),bg="red3",fg="yellow")
l1.grid(row=0,column=11,columnspan=3)
l2=Label(window,text="PLAYER 1:X",font=("Comic Sans MS",'20'),bg="mediumpurple3",fg="navyblue")
l2.grid(row=1,column=15)
l3=Label(window,text="PLAYER 2:O",font=("Comic Sans MS",'20'),bg="mediumpurple3",fg="navyblue")
l3.grid(row=1 ,column=17)

img=PhotoImage(file="p2.png")
d1=Label(window,image=img)
d1.grid(row=2,column=15,columnspan=3,rowspan=4)


def intial():
    global wins
    global win
    win=0
    wins=0
    l6=Label(window,text=wins,font=("Comic Sans MS",'15'), bg="mediumpurple3")
    l6.grid(row=2,column=15)
    l5=Label(window,text=win,font=("Comic Sans MS",'15'), bg="mediumpurple3")
    l5.grid(row=2,column=17)
    
intial()    

t=1  
def play1():
    global t
    if b1["text"]==" ":
        if t==1:
            t=2
            b1.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b1.configure(text="O",fg="blue")
        decision()
def play2():
    global t
    if b2["text"]==" ":
        if t==1:
            t=2
            b2.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b2.configure(text="O",fg="blue")
        decision()
def play3():
    global t
    if b3["text"]==" ":
        if t==1:
            t=2
            b3.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b3.configure(text="O",fg="blue")
        decision()
def play4():
    global t
    if b4["text"]==" ":
        if t==1:
            t=2
            b4.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b4.configure(text="O",fg="blue")
        decision()
def play5():
    global t
    if b5["text"]==" ":
        if t==1:
            t=2
            b5.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b5.configure(text="O",fg="blue")
        decision()
def play6():
    global t
    if b6["text"]==" ":
        if t==1:
             t=2
             b6.configure(text="X",fg="yellow")
        elif t==2:
             t=1
             b6.configure(text="O",fg="blue")
        decision()
def play7():
    global t
    if b7["text"]==" ":
        if t==1:
            t=2
            b7.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b7.configure(text="O",fg="blue")
        decision()
def play8():
    global t
    if b8["text"]==" ":
        if t==1:
            t=2
            b8.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            
            b8.configure(text="O",fg="blue")
        decision()
def play9():
    global t
    if b9["text"]==" ":
        if t==1:
            t=2
            b9.configure(text="X",fg="yellow")
        elif t==2:
            t=1
            b9.configure(text="O",fg="blue")
        decision()
tie=1    
def decision():
    global tie
    a1 = b1["text"];
    a2 = b2["text"];
    a3 = b3["text"];
    a4 = b4["text"];
    a5 = b5["text"];
    a6 = b6["text"];
    a7 = b7["text"];
    a8 = b8["text"];
    a9 = b9["text"];
    
    tie=tie+1
        
    if a1==a2 and a1==a3 and a1=="O" or a1==a2 and a1==a3 and a1=="X":
       
        w(b1["text"])
    if a4==a5 and a4==a6 and a4=="O" or a4==a5 and a4==a6 and a4=="X":
        w(b4["text"])
    if a7==a8 and a7==a9 and a7=="O" or a7==a8 and a7==a9 and a7=="X":
        w(b7["text"])
    if a1==a4 and a1==a7 and a1=="O" or a1==a4 and a1==a7 and a1=="X":
        w(b1["text"])
    if a2==a5 and a2==a8 and a2=="O" or a2==a5 and a2==a8 and a2=="X":
        w(b2["text"])
    if a3==a6 and a3==a9 and a3=="O" or a3==a6 and a3==a9 and a3=="X":
        w(b3["text"])
    if a1==a5 and a1==a9 and a1=="O" or a1==a5 and a1==a9 and a1=="X":
        w(b1["text"])
    if a7==a5 and a7==a3 and a7=="O" or a7==a5 and a7==a3 and a7=="X":
        w(b7["text"])
    if tie==10:
        messagebox.showinfo("Oops!!!"," Its a Tie!!!! Try again")
        reset()

wins=0
win=0
def w(player):
     global wins
     global win
     if(player=="X"):
        wins=wins+1
        messagebox.showinfo("congratulations!!",'Player 1 gets a point ')
        l4=Label(window,text=wins,font=("Comic Sans MS",'20'), bg="mediumpurple3")
        l4.grid(row=2,column=15)
        reset()
     else:
        messagebox.showinfo("congratulations!!"," Player 2 gets a point")
        win=win+1
        l5=Label(window,text=win,font=("Comic Sans MS",'20'), bg="mediumpurple3")
        l5.grid(row=2,column=17)
        reset()
        
def final():
    if(wins==win):
         messagebox.showinfo("Oops!!","Its a tie!!! Try again ")
         window.destroy()
    elif(wins>win):
        messagebox.showinfo("congratulations!!","Player 1 is the winner")
        window.destroy()
    else:
        messagebox.showinfo("congratulations!!","Player 2 is the winner")
        window.destroy()
def reset():
  global b1
  b1 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play1,relief="raised",borderwidth="13")
  b1.grid(column=2, row=3)
  global b2
  b2 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play2,relief="raised",borderwidth="13")
  b2.grid(column=4, row=3)
  global b3
  b3 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play3,relief="raised",borderwidth="13")
  b3.grid(column=5, row=3)
  global b4
  b4 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play4,relief="raised",borderwidth="13")
  b4.grid(column=2, row=4)
  global b5
  b5 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play5,relief="raised",borderwidth="13")
  b5.grid(column=4, row=4)
  global b6
  b6 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play6,relief="raised",borderwidth="13")
  b6.grid(column=5, row=4)
  global b7
  b7 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play7,relief="raised",borderwidth="13")
  b7.grid(column=2, row=5)
  global b8
  b8 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play8,relief="raised",borderwidth="13")
  b8.grid(column=4, row=5)
  global b9
  b9 = Button(window, text=" ",bg="brown2", fg="yellow",width=10,height=4,font=('comic sans','20'),command=play9,relief="raised",borderwidth="13")
  b9.grid(column=5, row=5)
  global t
  t=1
  global tie
  tie=1

def resetg():
    global wins
    wins=0
  
reset()
bu=Button(window,text="RESET",bg="yellow",fg="red",command=reset,width=8,height=3,borderwidth="9",font=("Comic Sans MS",'9'))
bu.grid(column=16,row=5)
but=Button(window,text="EXIT",bg="white",command=final,width=8,height=3,borderwidth="9",font=("Comic Sans MS",'9'))
but.grid(column=14,row=5)
but1=Button(window,text="RESET GAME",bg="green",fg="pink",command=intial,width=10,height=3,borderwidth="9",font=("Comic Sans MS",'9'))
but1.grid(column=18,row=5)

window.mainloop()
