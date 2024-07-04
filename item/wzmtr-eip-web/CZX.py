'''
coding:utf-8
@Software:PyCharm
@Time:2023/2/21 14:50
@Author:haidong
'''

import random
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk


def closeWindow():
    messagebox.showinfo(title="警告", message="确认要关闭该窗口吗？")
    return


def tongyi():
    win = tk.Toplevel(window)
    win.geometry("500x150+{}+{}".format(int((screenwidth - width) / 2), int((screenheight - height) / 2)))
    win.title("辞职")
    label = tk.Label(win, text="老板大人，臣告退了，这一退，可能\n就是一辈子了，\n！！！！！∠(°ゝ°)敬礼", font=("华文行楷", 20))
    label.pack()

    btn = tk.Button(win, text="拜拜", width=10, height=2, command=window.destroy)
    btn.pack()


def butongyi():
    B2.place_forget()
    B2.place(x=random.randint(100, 600), y=random.randint(100, 600))


if __name__ == '__main__':
    window = tk.Tk()
    window.title('辞职信')
    width = 600
    height = 600

    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    window.resizable(width=False, height=True)
    window.geometry('600x600')

    window.protocol("WM_DELETE_WINDOW", closeWindow)

    L1 = tk.Label(window, text='尊敬的各位领导：')
    L1.place(x=100, y=100)

    # 打开引用图片位置0
    load = Image.open('CIZHI.gif')
    render = ImageTk.PhotoImage(load)
    L2 = tk.Label(window, image=render)
    L2.place(x=200, y=100)

    B1 = tk.Button(window, text='同意', command=tongyi)
    B1.place(x=100, y=250)

    B2 = tk.Button(window, text='不同意', command=butongyi)
    B2.place(x=200, y=250)

    window.mainloop()
