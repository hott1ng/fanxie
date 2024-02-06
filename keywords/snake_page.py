from fight_page import FightPage

from airtest.core.api import *


class SnakePage(FightPage):


    def __init__(self):
        super().__init__()


    def double_fight(self):
        pass


    def enter_yeyuanhuo(self):
        pass


    def fight_yeyuanhuo(self):
        pass

    def quit_yeyuanhuo(self):
        self.quit()



    def yeyuanhuo_run(self):
        self.start()

        self.monitor_fight()

        self.monitor_win()


