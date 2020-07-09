import time
from manager import *
from order import *
import pandas as pd

def main():
    manager = Manager()
    manager.set_input_path("/Users/Mohan/Desktop/EasyOrder/EasyOrder/Orders")
    manager.read_input_dir()
    #manager.sort_edd()


if __name__ == "__main__":
    main()