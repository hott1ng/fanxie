from keywords.fight_page import FightPage
from airtest.core.api import *

class CrossFightPage(FightPage):
    attack_button_template = Template()


    def enter_crossfight(self):
        # 从庭院出发

        # 点击探索

        touch()

        # 点击结界突破
        touch()


    def one_round(self):
        # 退四打九
        # 定位九宫格


        # 退四
        # 点击进攻
        touch()
        for i in range(4):


            # 等待加载
            sleep(1)

            # 点击退出
            touch()

            # 点击重新挑战
            touch()





        pass


    def main(self):
        pass
