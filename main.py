import os
import random
import tkinter
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image,ImageTk
import backend
from backend import *

def switch(win,num):
    win.destroy()
    obj=cards()
    if num==1:
        obj.intro_win()
    elif num==2:
        obj.ist_win()
    return 1



class cards:
    def intro_win(self):
        win=Tk()
        win_seting(win, 1000, 600, "Luck by cards . . . ", "gray")
        create_image(win, "bg_image/luck.jpg",1000,600)
        next_B = Button(win, text="Let's GO", bg="#ffffff", font=("forte", 15), width="10",command=lambda: switch(win, 2))
        next_B.place(x=877, y=560)
        lab1 = Label(win, text="L ", height=1, width=5, fg="white", bg="blue",font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=0)
        lab1 = Label(win, text="U ", height=1, width=5, fg="white", bg="blue", font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=60)
        lab1 = Label(win, text="C ", height=1, width=5, fg="magenta", bg="blue", font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=120)
        lab1 = Label(win, text="K ", height=1, width=5, fg="magenta", bg="blue", font=("forty", 10, "bold"),   justify="center")
        lab1.place(x=0, y=200)


        lab1 = Label(win, text="G ", height=1, width=5, fg="white", bg="blue",font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=320)
        lab1 = Label(win,text="A ", height=1, width=5, fg="white", bg="blue", font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=420)
        lab1 = Label(win, text="M ", height=1, width=5, fg="magenta", bg="blue", font=("forty", 10, "bold"), justify="center")
        lab1.place(x=0, y=500)
        lab1 = Label(win, text="E ", height=1, width=5, fg="magenta", bg="blue", font=("forty", 10, "bold"),   justify="center")
        lab1.place(x=0, y=580)

        # ...............................
        lab1 = Label(win, text="L . U . C . K  G . A . M . E ", height=2, width=55, fg="magenta",bg="black",font=("forty", 20, "bold"),justify="center")
        lab1.place(x=48, y=0)
        lab1 = Label(win, text="Developed  ", height=2, width=12, fg="white", bg="black",font=("forty", 20, "bold"))
        lab1.place(x=48, y=50)
        lab1 = Label(win, text="BY  ", height=2, width=12, fg="blue", bg="black", font=("forty", 20, "bold"))
        lab1.place(x=48, y=100)
        lab1 = Label(win, text="Asad Bashir  ", height=5, width=12, fg="red", bg="black", font=("forty", 20, "bold"))
        lab1.place(x=48, y=150)
        # ..............................
        lab1 = Label(win, text="Dedicated  ", height=2, width=12, fg="white", bg="black", font=("forty", 20, "bold"))
        lab1.place(x=800, y=50)
        lab1 = Label(win, text="TO  ", height=2, width=12, fg="blue", bg="black", font=("forty", 20, "bold"))
        lab1.place(x=800, y=100)
        lab1 = Label(win, text="Sir Hassam  ", height=5, width=12, fg="red", bg="black", font=("forty", 20, "bold"))
        lab1.place(x=800, y=150)
        win.bind("<Button-3>",lambda event:location(event))
        win.mainloop()


    def ist_win(self):
        win=Tk()
        win_seting(win, 1000, 600, "Luck by cards . . . ", "gray")
        # print("in")
        create_image(win, "bg_image/bg2.jpg",1000,600)
        lab1=Label(win,text="Enter Your Lucky Number ",height=2,width=25,font=("forty",20,"bold"))
        lab1.place(x=48,y=26)
        lucky_num=Entry(win,bg="white",fg="black",font=("forte",45),width="3",justify="center")
        lucky_num.place(x= 510 ,y= 26)
        lucky_num.bind("<KeyRelease>",lambda event:check(event,lucky_num))

        fram1=Frame(win,width="200",height="250",bg="white")
        fram1.place(x=30+20,y=100)
        l1_label=Label(win,text="00",width=13,font=("forty",18,"bold"),justify="center")
        l1_label.place(x=50,y=400)
        create_image(fram1,"bg_image/bg2.jpg",200,250)

        fram2=Frame(win,width="200",height="250",bg="white")
        fram2.place(x=260+20,y=100)
        l2_label = Label(win,text="00", width=13, font=("forty", 18, "bold"), justify="center")
        l2_label.place(x=280, y=400)

        create_image(fram2, "resources/50.png",200,250)

        fram3=Frame(win,width="200",height="250",bg="white")
        fram3.place(x=490+20,y=100)
        l3_label = Label(win, text="00",width=13, font=("forty", 18, "bold"), justify="center")
        l3_label.place(x=520, y=400)
        create_image(fram3, "resources/1.png",200,250)

        fram4=Frame(win,width="200",height="250",bg="white")
        fram4.place(x=720+20,y=100)
        l4_label =Label(win,text="00", width=13, font=("forty", 18, "bold"), justify="center")
        l4_label.place(x=740, y=400)
        create_image(fram4,"resources/50.png",200,250)

        lab1 = create_image(fram1, "resources/3.png", 200, 250)
        lab2 = create_image(fram2, "resources/3.png", 200, 250)
        lab3 = create_image(fram3, "resources/3.png", 200, 250)
        lab4 = create_image(fram4, "resources/3.png", 200, 250)


        back_B = Button(win, text="Back", bg="#ffffff",fg="cyan4", font=("forte", 15), width="10", command=lambda: switch(win, 1))
        back_B.place(x=877, y=560)
        try_again =Label(win, text="..............", bg="#ffffff",fg="black", font=("forte", 22),height=2,width="27")
        try_again.place(x=280, y=460)
        done_buton=Button(win,text="Show Luck",width=24,height=2,fg="Black",bg="pink",command=lambda:change_image(lab1,lab2,lab3,lab4,lucky_num,done_buton,l1_label,l2_label,l3_label,l4_label,try_again),font=("forty",22,"bold"))
        done_buton.place(x=280,y=530)
        win.bind("<Button-3>",lambda event:location(event))
        win.mainloop()
        return 1


if __name__ == '__main__':
    obj=cards()
    obj.intro_win()