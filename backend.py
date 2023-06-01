import os
import random
import tkinter
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image,ImageTk
import main
from main import *

summ=0

num_list = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
num_list2 = [49, 50, 51, 52]
def win_seting(t_win,w,h,title,color):
    t_win.minsize(w, h)
    t_win.maxsize(w, h)
    main_screen_width = int(t_win.winfo_screenwidth() / 2)
    main_screen_height = int(t_win.winfo_screenheight() / 2)
    t_win.geometry(f"{w}x{h}+{main_screen_width - int((w / 2))}+{main_screen_height - int((h / 2)+50)}")
    t_win.title(title)
    t_win.config(bg=color)
    # win.iconbitmap("")
    return 1

def s_slide_image(label,label2):
    x=0
    y=0
    # x = 490 + 20, y = 100
    while  True:
        while y<=250:
            y+=3
            label.place(x=x,y=y)
            label2.place(x=x,y=y)
            label.update()
            label2.update()
            label.after(10)
            label2.after(10)
        label.place(x=x, y=y)
        label2.place(x=x,y=y)
        x=0
        y=0

def create_image(frame,imgpath,w,h):
    img=Image.open(imgpath).resize((w,h))
    imgtk=ImageTk.PhotoImage(img)
    lab=Label(frame)
    lab.config(image=imgtk,bd=0)
    lab.image=imgtk
    lab.place(x=0,y=0)
    return lab

def check(event,ent_box):
    lis=['0','1','2','3','4','5','6','7','8','9']
    print(event.char)
    if event.char in lis:
        data=ent_box.get()
        if len(data)>1:
            ent_box.delete(0,END)
            ent_box.insert(0,data[0])
    else:
        ent_box.delete(0, END)

def location(event):
    print("x=",event.x,",y=",event.y)
    return 1


def change_image(lab1,lab2,lab3,lab4,lucky_num,done_button,f1_label,f2_label,f3_label,f4_label,luck_per):
    global num_list,num_list2
    global summ
    luck_num=lucky_num.get()
    if luck_num=="":
        messagebox.showerror("Error","Enter Lucky Number")
    else:
        def lab2_image_display(i):
            global summ
            if i < 10:
                num = random.randint(1, 52)
                path=f"resources/{num}.png"
                # path = f"resources/{num}.png"
                img = Image.open(path)
                img_tk = ImageTk.PhotoImage(img)

                # Update the label with the new image
                lab2.config(image=img_tk, bd=0)
                lab2.image = img_tk
                lab2.after(100, lab2_image_display, i + 1)
                if num in num_list:
                    f2_label.config(text="10")
                    if i==9:
                        summ+=10
                elif num in num_list2:
                    f2_label.config(text="20")
                    if i==9:
                        summ+=20
                else:
                    f2_label.config(text="05")
                    if i==9:
                        summ+=5
        def lab3_image_display(i):
            global summ
            if i < 10:
                num = random.randint(1, 52)
                path =f"resources/{num}.png"
                img = Image.open(path)
                img_tk = ImageTk.PhotoImage(img)
                lab3.config(image=img_tk, bd=0)
                lab3.image = img_tk
                lab3.after(100, lab3_image_display, i + 1)
                if num in num_list:
                    f3_label.config(text="10")
                    if i==9:
                        summ+=10
                elif num in num_list2:
                    f3_label.config(text="20")
                    if i==9:
                        summ+=20
                else:
                    f3_label.config(text="05")
                    if i == 9:
                        summ += 5
        def lab4_image_display(i):
            global summ
            if i < 10:
                num = random.randint(1, 52)
                path =f"resources/{num}.png"
                # path = f"resources/{num}.png"
                img = Image.open(path)
                img_tk = ImageTk.PhotoImage(img)
                lab4.config(image=img_tk, bd=0)
                lab4.image = img_tk
                lab4.after(100, lab4_image_display, i + 1)
                if num in num_list:
                    f4_label.config(text="10")

                    if i==9:
                        summ+=10
                elif num in num_list2:
                    f4_label.config(text="20")
                    if i==9:
                        summ+=20
                else:
                    f4_label.config(text="05")
                    if i==9:
                        summ+=5
            else:
                percentage = (summ / 80) * 100
                luck_per.config(text=f"Today yOU Are {percentage}% Lucky")
                summ=0
        def display_image(i):
            global summ
            num_list = [37,38,39,40, 41, 42, 43, 44, 45, 46, 47, 48]
            num_list2 = [49, 50, 51, 52]
            if i < 10:
                done_button.config(state="disable")
                num = random.randint(1, 52)
                path =f"resources/{num}.png"
                img = Image.open(path)
                img_tk = ImageTk.PhotoImage(img)
                lab1.config(image=img_tk, bd=0)
                lab1.image = img_tk
                lab1.after(100, display_image, i + 1)
                if num in num_list:
                    f1_label.config(text="10")
                    if i == 9:
                        summ += 10
                elif num in num_list2:
                    f1_label.config(text="20")
                    if i==9:
                        summ+=20
                else:
                    f1_label.config(text="05")
                    if i==9:
                        summ+=5
            else:
                done_button.config(state="normal")
        display_image(0)
        lab2_image_display(0)
        lab3_image_display(0)
        lab4_image_display(0)
def location(event):
    print("x=",event.x,",y=",event.y)


