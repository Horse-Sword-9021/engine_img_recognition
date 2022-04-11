from tkinter import *
import time

from numpy import place

root = Tk()
root.geometry('1200x690')
root.title('Engine_img_recognition')
background_img = PhotoImage(file='background.png')

canvs = Canvas(root, bg='blue', width=1200, height=580)
canvs.create_image(600, 290, anchor=CENTER, image=background_img)
canvs.pack()

Label(root, text='简介', fg='black', font=("宋体", 25)).place(x=100, y=150, anchor=W)
Label(root, text='欢迎使用Engine_img_recognition，本软件系统可用于处理图像、识别航空发动机缺陷\n本软件用python编写所需代码，设计GUI界面', fg='black',
      font=("宋体", 21)).place(x=100, y=200, anchor=W)

Label(root, text='作者', fg='black', font=("宋体", 25)).place(x=100, y=300, anchor=W)
Label(root, text='马剑', fg='black', font=("宋体", 20)).place(x=200, y=300, anchor=W)
Label(root, text='菜单栏:', fg='black', bg='gray', font=("宋体", 21)).place(x=200, y=650, anchor=CENTER)

lb = Label(root, text='请选择', fg='black', font=("宋体", 22))
lb.pack()


def main_menu():
    dic = {0: '图像处理', 1: '识别图片（发动机缺陷识别）', 2: '开发者选项', 3: '退出'}
    s = "您选了" + dic.get(var.get()) + "项"
    lb.config(text=s)


var = IntVar()
rd1 = Button(root, text="1、图像处理", width=15, height=2, anchor=CENTER,
             command=main_menu)  # ,width=15,height=2,command=Mysel)
rd1.place(x=370, y=650, anchor=CENTER)
var = IntVar()
rd2 = Button(root, text='2、识别图片(发动机缺陷识别)', width=25, height=2, anchor=CENTER, command=main_menu)
rd2.place(x=540, y=650, anchor=CENTER)
var = IntVar()
rd3 = Button(root, text="3、开发者选项", width=15, height=2, anchor=CENTER, command=main_menu)
rd3.place(x=710, y=650, anchor=CENTER)
var = IntVar()
rd4 = Button(root, text="4、退出", width=15, height=2, anchor=CENTER, command=main_menu)
rd4.place(x=850, y=650, anchor=CENTER)

root.mainloop()
# from tkinter import *
# import time
#
#
# def main_menu():
#     dic = {0: '处理图片', 1: '识别图片', 2: '开发者选项', 3: '退出'}
#     s = "您选了" + dic.get(var.get()) + "项"
#     lb.config(text=s)
#
#
# def image_preprocess_menu():
#     dic = {0: '处理图片', 1: '识别图片', 2: '开发者选项', 3: '退出'}
#     s = "您选了" + dic.get(var.get()) + "项"
#     lb.config(text=s)
#
#
# root = Tk()
# root.geometry('1200x690')
# root.title('Engine_img_recognition')
# background_img = PhotoImage(file='background.png')
#
# canvs = Canvas(root, bg='blue', width=1200, height=580)
# canvs.create_image(600, 290, anchor=CENTER, image=background_img)
# canvs.pack()
# lb = Label(root, text='欢迎使用Engine_img_recognition，本软件系统可用于处理图像、识别航空发动机缺陷', fg='black', font=("宋体", 21))
# lb.pack()
#
# var = IntVar()
# rd1 = Button(root, text="1、处理图片", width=15, height=2, anchor=CENTER, command=main_menu)  # ,width=15,height=2,command=Mysel)
# rd1.place(x=390, y=650, anchor=CENTER)
#
# rd2 = Button(root, text="2、识别图片", width=15, height=2, anchor=CENTER, command=main_menu)
# rd2.place(x=540, y=650, anchor=CENTER)
#
# rd3 = Button(root, text="3、开发者选项", width=15, height=2, anchor=CENTER, command=main_menu)
# rd3.place(x=690, y=650, anchor=CENTER)
#
# rd4 = Button(root, text="4、退出", width=15, height=2, anchor=CENTER, command=main_menu)
# rd4.place(x=840, y=650, anchor=CENTER)
#
# root.mainloop()
