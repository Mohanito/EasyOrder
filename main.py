import time
from manager import *
from order import *
import pandas as pd

def main():
    manager = Manager()
    '''
    manager.tujiao_speed = input("输入涂胶速度：")
    manager.zhijiao_tujiao = input("输入直角涂胶时间：")
    manager.wait_time = input("输入等待时间：")
    manager.switch_time = input("输入切换时间：")
    '''
    manager.set_input_path("/Users/Mohan/Desktop/EasyOrder/EasyOrder/Orders")
    manager.read_input_dir()
    #manager.sort_edd()


if __name__ == "__main__":
    main()