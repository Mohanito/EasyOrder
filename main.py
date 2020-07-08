import time
from manager import *
from order import *
import pandas as pd

def main():
    manager = Manager()
    manager.update_sot()
    sheet = pd.read_excel('order_list.xlsx', sheet_name = 'Sheet1')
    print("Column headings:")
    print(sheet.columns)

if __name__ == "__main__":
    main()