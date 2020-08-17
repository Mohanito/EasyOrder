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

    button = tk.Button(frame, text = '运行', bg = 'white', command = lambda: GUI_on_click(lower_label, manager, entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    button.place(relx = 0.45, rely = 0.9)

    lower_frame = tk.Frame(frame)
    lower_frame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.4, anchor='n')

    lower_label = tk.Label(lower_frame, bg = 'white')
    lower_label.place(relwidth = 1, relheight = 1)
    lower_label['text'] = '欢迎使用\n请填入数据，然后点击运行'

    root.mainloop()
    
    # tkinter UI ends


def GUI_on_click(lower_label, manager, tujiao_speed, zhijiao_tujiao, wait_time, switch_time):
    if not(tujiao_speed.isnumeric() and zhijiao_tujiao.isnumeric() and wait_time.isnumeric() and switch_time.isnumeric()):
        lower_label['text'] = '请填入整数'
    else:
        manager.tujiao_speed = float(tujiao_speed)
        manager.zhijiao_tujiao = float(zhijiao_tujiao)
        manager.wait_time = float(wait_time)
        manager.switch_time = float(switch_time)
        lower_label['text'] = 'data type correct'
        try:
            manager.read_input_dir()
            manager.output()
            lower_label['text'] += '\ndone, please check result.xls'
        except:
            lower_label['text'] = 'Unexpected error'    # tested, works


if __name__ == "__main__":
    main()