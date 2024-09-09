from base_page import BasePage
from airtest.core.api import *
from keywords.download_page import DownloadPage
from keywords.fight_page import  FightPage


class MiwenPage(BasePage):
    cancel_template = Template(r'static/app/庭院/取消.png')
    close_template = Template(r'static/app/庭院/关闭.png')


    def main(self):
        # 启动

        DownloadPage().main()

        sleep(15)

        sleep(3)

        try:
            if exists(self.cancel_template):
                touch(self.cancel_template)
            elif exists(self.close_template):
                touch(self.close_template)
        except:
            pass

        # 从庭院出发，点击探索
        touch(self.tansuo_template)

        # 点击秘闻按钮
        touch()

        sleep(5)
        # 点击一下，关闭广告
        touch(1,1)

        # 点击式神录
        touch()


        # 更换御魂
        touch()

        # 退出式神录
        touch()

        # 点击进入
        touch()

        # 点击战斗
        touch()

        # 点击准备
        touch()

        # 退出战斗
