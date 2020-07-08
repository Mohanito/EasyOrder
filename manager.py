import pandas as pd

class Manager:
    def __init__(self):
        self.input_path = ""
        self.order_list = []
        self.dataframe = pd.DataFrame()
        self.num_orders = 0

    def set_input_path(self, path):
        self.input_path = path

    def read_excel(self):
        print("Reading input file...")
        self.dataframe = pd.read_excel('order_list.xlsx', sheet_name = 'Sheet1')
        temp_series = self.dataframe[self.dataframe.columns[0]]
        self.num_orders = temp_series[1:].max()
        print("# of orders: " + str(self.num_orders))