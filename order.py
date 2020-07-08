class Order:
    def __init__(self):
        EDD = 0
        SOT = 0     # needs to be calculated
        STR = 0
    def update_sot(self):
        # 总工时（秒）=
        # (每个订单号的玻璃累计周长/涂胶速度）+（每片玻璃直角的涂胶时间*4*玻璃片数）
        # +（等待时间*玻璃片数）+（切换时间*玻璃片数/35）
        print("hello")