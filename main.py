import time
from manager import *
from order import *
import pandas as pd

def main():
    manager = Manager()
    input_path = 'order_list.xlsx'
    manager.set_input_path(input_path)
    manager.read_excel()


if __name__ == "__main__":
    main()