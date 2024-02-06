from airtest.core.api import *
from keywords.base_page import BasePage



class FightPage(BasePage):
    fight_button_template = Template()
    win_button_template = Template()
    back_button_template = Template()


    def __init__(self):
        pass

    def monitor_win(self):
        pos = wait()
        return pos
        pass

    def monitor_fight(self):
        pos = wait()
        return pos

    def start(self):
        pass


    def back(self):
        pass

    def quit(self):
        pass

    def replace_yuhun(self, group, name):
        # 从庭院更换

        # 点击卷轴
        touch()

        # 点击式神
        touch()

        # 点击预设
        touch()

        # 点击日常
        touch()

        # 寻找业原火方案，若无滑动
        if exists():
            touch()
        else:
            swipe()


        # 点击确定
        touch()

        # 返回庭院
        touch()

