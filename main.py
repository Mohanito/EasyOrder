import time
import tkinter as tk
from manager import *
from order import *
import pandas as pd

bg_color = '#b7d7e8'

def main():

    manager = Manager()
    manager.set_input_path("/Users/Mohan/Desktop/EasyOrder/EasyOrder/new_order_set")

    # Tkinter UI
    root = tk.Tk()

    canvas = tk.Canvas(root, height = 600, width = 600)
    canvas.pack()

    frame = tk.Frame(root, bg = bg_color)
    frame.place(relwidth = 1, relheight = 1)

    entry1 = tk.Entry(frame, bg = 'white', font = 32)
    entry1.place(x = 150, y = 50)
    entry2 = tk.Entry(frame, bg = 'white', font = 32)
    entry2.place(x = 150, y = 100)
    entry3 = tk.Entry(frame, bg = 'white', font = 32)
    entry3.place(x = 150, y = 150)
    entry4 = tk.Entry(frame, bg = 'white', font = 32)
    entry4.place(x = 150, y = 200)
    entry5 = tk.Entry(frame, bg = 'white', font = 32)
    entry5.place(x = 150, y = 250)

    label1 = tk.Label(frame, text = '输入涂胶速度：', bg = bg_color)
    label1.place(x = 0, y = 50)
    label2 = tk.Label(frame, text = '输入直角涂胶时间：', bg = bg_color)
    label2.place(x = 0, y = 100)
    label3 = tk.Label(frame, text = '输入等待时间：', bg = bg_color)
    label3.place(x = 0, y = 150)
    label4 = tk.Label(frame, text = '输入切换时间：', bg = bg_color)
    label4.place(x = 0, y = 200)

    label5 = tk.Label(frame, text = '米/分钟', bg = bg_color)
    label5.place(x = 350, y = 50)
    label6 = tk.Label(frame, text = '秒', bg = bg_color)
    label6.place(x = 350, y = 100)
    label7 = tk.Label(frame, text = '秒', bg = bg_color)
    label7.place(x = 350, y = 150)
    label8 = tk.Label(frame, text = '秒', bg = bg_color)
    label8.place(x = 350, y = 200)

    label9 = tk.Label(frame, text = '标准作业时间：', bg = bg_color)
    label9.place(x = 0, y = 250)
    label10 = tk.Label(frame, text = '小时', bg = bg_color)
    label10.place(x = 350, y = 250)

    rb_var = tk.IntVar()    # num_shift

    button = tk.Button(frame, text = '运行', bg = 'white', command = lambda: GUI_on_click(lower_label, manager, entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), rb_var))
    button.place(relx = 0.45, rely = 0.9)

    rb1 = tk.Radiobutton(frame, text = '单班作业制', variable = rb_var, value = 1, command = lambda: rb_on_click(manager, rb_var))
    rb1.place(x = 400, y = 200)
    rb2 = tk.Radiobutton(frame, text = '双班作业制', variable = rb_var, value = 2, command = lambda: rb_on_click(manager, rb_var))
    rb2.place(x = 400, y = 250)

    lower_frame = tk.Frame(frame)
    lower_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.35, anchor='n')

    lower_label = tk.Label(lower_frame, bg = 'white')
    lower_label.place(relwidth = 1, relheight = 1)
    lower_label['text'] = '欢迎使用\n请填入数据，然后点击运行'

    root.mainloop()
    
    # tkinter UI ends


def GUI_on_click(lower_label, manager, tujiao_speed, zhijiao_tujiao, wait_time, switch_time, shift_length, rb_var):
    if not(tujiao_speed.isnumeric() and zhijiao_tujiao.isnumeric() and wait_time.isnumeric() and switch_time.isnumeric() and shift_length.isnumeric()):
        lower_label['text'] = '请填入整数'
    elif not (rb_var.get() == 1 or rb_var.get() == 2):
        lower_label['text'] = '请选择单/双班作业制'
    else:
        manager.tujiao_speed = float(tujiao_speed)
        manager.zhijiao_tujiao = float(zhijiao_tujiao)
        manager.wait_time = float(wait_time)
        manager.switch_time = float(switch_time)
        manager.shift_length = float(shift_length)
        lower_label['text'] = '数据符合要求'
        try:
            manager.read_input_dir()    # orders get duplicated on click
            manager.output()
            lower_label['text'] += '\n已完成, 输出表格为result.xls'
            lower_label['text'] += '\n请关闭窗口，勿再次点击运行按钮'
        except:
            lower_label['text'] = 'Unexpected error'    # tested, works

def rb_on_click(manager, rb_var):
    # 单/双班工作制
    # print(rb_var.get())
    manager.num_shift = rb_var.get()


if __name__ == "__main__":
    main()