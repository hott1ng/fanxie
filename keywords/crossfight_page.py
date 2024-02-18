from keywords.fight_page import FightPage
from airtest.core.api import *
from goto_page import GotoPage


class CrossFightPage(FightPage):
    attack_button_template = Template()

    def enter_crossfight(self):
        # 从庭院出发点击探索
        GotoPage().goto_tansuo()

        # 点击结界突破
        touch()

    def one_round(self):
        # 退四打九
        # 定位九宫格

        # 退四
        # 点击进攻
        touch()
        for i in range(3):
            # 等待加载
            sleep(5)

            # 点击退出
            touch()

            # 点击重新挑战
            touch()

        # 退出
        touch()

        # 打九
        for i in range(9):
            # 点击进攻
            touch()
            sleep(3)

            prepare_pos = self.monitor_prepare()
            touch(prepare_pos)

            if self.monitor_win():
                # 开始执行领取奖励

                # 点第一个地方
                touch()

                sleep(3)

                # 点第二个地方
                touch()

        pass

    def main(self):
        pass
