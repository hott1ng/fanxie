from airtest.core.api import *
from base_page import BasePage
import os


class DownloadPage(BasePage):
    click_to_start_button_template = Template(r'static/app/登录界面/进入游戏.png')
    # change_player_button_template = Template()
    desktop_icon = Template(r'static/desktop/桌面图标.png')
    age_icon = Template(r'static/app/登录界面/用于判断登录界面.png')


    # 随便放一张
    update_button = Template('static/app/庭院/庭院卷轴.png')

    def download(self):
        self.base_start()
        print(os.getcwd())
        for i in range(3):
            sleep(3)
            touch((100, 100))
            sleep(3)
            touch((100, 100))

            self.update_app()

            try:
                if wait(self.age_icon):
                    sleep(7)
                    touch(self.click_to_start_button_template)
                    print("进入游戏成功")
                    break

            except TargetNotFoundError:
                print("没找到进入游戏按钮")



    def change_player(self):
        touch(self.change_player_button_template)

    def update_app(self):
        if exists(self.update_button):
            touch(self.update_button)
            sleep(180)
            print("需要更新")


    def main(self):
        self.download()


if __name__ == '__main__':
    aa = DownloadPage()
    aa.download()
    # aa.base_stop()