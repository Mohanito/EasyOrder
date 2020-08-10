import pandas as pd
from order import *
import os
import xlwt

HEADINGS = ["序号", "项目名称", "订单号", "产品配置", "单片玻璃种类", "单片玻璃厚度(mm)", 
            "总片数", "总面积(m^2)", "长边单侧累计长度(mm)", "总周长(mm)", "", "交货日期",
            "EDD", "SOT", "STR", "订单延迟时间"]

class Manager:
    def __init__(self):
        self.input_path = ""
        self.order_list = []
        self.dataframe = pd.DataFrame()
        self.num_orders = 0

        # below are user inputs
        self.tujiao_speed = 29 # 米/分钟
        self.zhijiao_tujiao = 3 # 秒
        self.wait_time = 1 #秒
        self.switch_time = 60 #秒

    def set_input_path(self, path):
        self.input_path = path

    def read_input_dir(self):
        for filename in os.listdir(self.input_path):
            if ".xls" in filename:
                new_order = Order(self.input_path + '/' + filename)
                new_order.read_input()
                # （每个订单号的玻璃累计周长（米）/涂胶速度(input)）+ 每片玻璃直角的涂胶时间(input)*4*玻璃片数）+（等待时间(input)*玻璃片数）+（切换时间(input)*玻璃片数/35）
                new_order.SOT = (new_order.total_circumference / self.tujiao_speed) + (self.zhijiao_tujiao * 4 * new_order.amount) + (self.wait_time + new_order.amount) + (self.switch_time * new_order.amount / 35)
                self.order_list.append(new_order)

    def output(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Sheet1')
        # Sort using EDD
        self.order_list.sort(key = lambda x: x.EDD, reverse = False)

        for i in range(len(HEADINGS)):
            sheet.write(0, i, HEADINGS[i])
        
        for i in range(len(self.order_list)):
            current_order = self.order_list[i]
            sheet.write(i + 1, 0, i + 1)
            sheet.write(i + 1, 2, current_order.order_num)
            sheet.write(i + 1, 3, current_order.order_code)
            sheet.write(i + 1, 6, current_order.amount)
            sheet.write(i + 1, 7, current_order.total_area)
            sheet.write(i + 1, 8, current_order.total_longer)
            sheet.write(i + 1, 9, current_order.total_circumference)
            date_format = xlwt.XFStyle()
            date_format.num_format_str = 'yyyy/mm/dd'
            sheet.write(i + 1, 11, current_order.deadline, date_format)
            sheet.write(i + 1, 12, current_order.EDD)
            sheet.write(i + 1, 13, current_order.SOT)
        workbook.save('result.xls')

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