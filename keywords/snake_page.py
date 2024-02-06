from fight_page import FightPage

from airtest.core.api import *


class SnakePage(FightPage):
    fight_button_template = Template()
    prepare_button_template = Template()


    def __init__(self):
        super().__init__()


    def click_fight(self):
        touch(self.fight_button_template)

    def click_prepare(self):
        for i in range(10):
            try:
                pos = wait(self.prepare_button_template, timeout=10)
                touch(pos)
                break

            except TargetNotFoundError:
                print("未找到准备按钮，重试中...")

            if i == 9:
                print("未找到准备按钮，退出游戏")


    def double_fight(self):
        pass


    def enter_yeyuanhuo(self):
        pass


    def fight_yeyuanhuo(self):
        self.click_fight()
        sleep(5)
        self.click_prepare()

    def quit_yeyuanhuo(self):
        self.quit()


    def yeyuanhuo_enter(self):
        # 从庭院进入业原火

        # 点击探索
        touch()

        # 点击御魂
        touch()

        # 点击业原火
        touch()

        # 点击高级
        touch()








    def yeyuanhuo_run(self):
        self.replace_yuhun()

        self.enter_yeyuanhuo()

        while True:


