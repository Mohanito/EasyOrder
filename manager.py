import pandas as pd
from order import *
import os


class Manager:
    def __init__(self):
        self.input_path = ""
        self.order_list = []
        self.dataframe = pd.DataFrame()
        self.num_orders = 0

        # below are user inputs
        self.tujiao_speed = 0
        self.zhijiao_tujiao = 0
        self.wait_time = 0
        self.switch_time = 0

    def set_input_path(self, path):
        self.input_path = path

    def read_input_dir(self):
        for filename in os.listdir(self.input_path):
            if ".xls" in filename:
                new_order = Order(self.input_path + '/' + filename)
                new_order.read_input()
                # new_order.print_order_details()
        self.order_list.append(new_order)


    # old method using pandas
    '''
    def read_excel(self):
        print("Reading input file...")
        self.dataframe = pd.read_excel('order_list.xlsx', sheet_name = 'Sheet1')
        index_series = self.dataframe[self.dataframe.columns[0]]
        self.num_orders = index_series[1:].max()
        print("# of orders: " + str(self.num_orders))
        # Updating order list
        deadline_series = self.dataframe[self.dataframe.columns[11]]
        
        for i in range(1, self.num_orders + 1):
            new_order = Order(deadline_series[i], self.dataframe["SOT"][i], i)
            self.order_list.append(new_order)
    '''

    def sort_edd(self):
        self.order_list.sort(key = lambda x: x.EDD, reverse = False)
        for order in self.order_list:
            print(str(order.order_index) + ": EDD = " + str(order.EDD))

    def sort_sot(self):
        self.order_list.sort(key = lambda x: x.SOT, reverse = False)
        for order in self.order_list:
            print(str(order.order_index) + ": SOT = " + str(order.SOT))
    
    def sort_str(self):
        pass