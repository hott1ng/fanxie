from airtest.core.api import *
from keywords.base_page import BasePage


class FightPage(BasePage):
    fight_button_template = Template()
    win_button_template = Template()
    back_button_template = Template()

    prepare_button_template = Template()

    def __init__(self):
        pass

    def monitor_win(self):
        pos = wait()
        for i in range(10):
            if pos:
                return True
            else:
                sleep(10)
        raise TargetNotFoundError("无法达到胜利界面")


    def monitor_fight(self):
        pos = wait()
        return pos

    def monitor_prepare(self):
        for i in range(10):
            pos = wait()
            if pos:
                return pos
        raise TargetNotFoundError("准备按钮未找到")

    def start(self):
        pass

    def back(self):
        pass

    def quit(self):
        pass

    def receive_reward(self):
        while True:
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
