import pandas as pd
import datetime
import xlrd

class Order:
    def __init__(self, path):
        self.workbook = xlrd.open_workbook(path)
        self.worksheet = self.workbook.sheet_by_name('Sheet1')
        self.order_num = ""
        self.order_code = ""
        self.deadline = 0
        self.EDD = 0
        self.amount = 0
        # TODO:
        self.SOT = 0#SOT  # needs to be calculated
        self.STR = 0
    
    def read_input(self):
        self.order_num = self.worksheet.cell(3, 3).value
        self.order_code = self.worksheet.cell(7, 4).value
        self.deadline = xlrd.xldate.xldate_as_datetime(self.worksheet.cell(9, 24).value, self.workbook.datemode)
        self.EDD = (self.deadline - datetime.datetime.now()).days
        self.amount = self.worksheet.cell(7, 32).value
        print(self.amount)


    def print_order_details(self):
        print("Order {}".format(str(self.order_num)))
        print("EDD = {}, SOT = {}, STR = {}\n".format(str(self.EDD), str(self.SOT), str(self.STR)))