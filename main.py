import time
import tkinter as tk
from manager import *
from order import *
import pandas as pd

def main():
    bg_color = '#d9ffde'

    root = tk.Tk()

    canvas = tk.Canvas(root, height = 400, width = 400)
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

    button = tk.Button(frame, text = 'RUN', bg = 'gray', command = lambda: GUI_read_input(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    button.place(relx = 0.45, rely = 0.9)

    root.mainloop()


    manager = Manager()
    '''
    manager.tujiao_speed = input("输入涂胶速度：")
    manager.zhijiao_tujiao = input("输入直角涂胶时间：")
    manager.wait_time = input("输入等待时间：")
    manager.switch_time = input("输入切换时间：")
    '''
    manager.set_input_path("/Users/Mohan/Desktop/EasyOrder/EasyOrder/new_order_set")
    manager.read_input_dir()
    manager.output()

def GUI_read_input(tujiao_speed, zhijiao_tujiao, wait_time, switch_time):
    print("涂胶速度 = {}".format(tujiao_speed))
    print("直角涂胶时间 = {}".format(zhijiao_tujiao))
    print("等待时间 = {}".format(wait_time))
    print("切换时间 = {}".format(switch_time))


if __name__ == "__main__":
    main()