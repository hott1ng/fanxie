from base_page import BasePage
from airtest.core.api import *



# 前往各个界面用到
class GotoPage(BasePage):

    tansuo_button_template  = Template()

    def goto_tansuo(self):
        # 从庭院出发
        touch()

    def goto_yinyangliao(self):
        touch()


    def goto_yuhun(self):
        # 先进入探索
        self.goto_tansuo()
        touch()


    def goto_digui(self):
        # 先进入探索
        self.goto_tansuo()
        touch()

    def goto_jiejie(self):
        self.goto_yinyangliao()
        touch()

    def back_tingyuan(self):
        touch()


