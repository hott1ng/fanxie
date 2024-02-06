from airtest.core.api import *
from base_page import BasePage


class DownloadPage(BasePage):
    click_to_start_button_template = Template(r'../static/app/登录界面/进入游戏.png')
    # change_player_button_template = Template()
    desktop_icon = Template(r'../static/desktop/桌面图标.png')

    def download(self):
        self.base_start()
        fail_times = 0
        while fail_times < 3:
            touch((100, 100))
            sleep(3)
            touch((100, 100))
            try:
                enter_pos = wait(self.click_to_start_button_template)
                sleep(3)
                touch(enter_pos)
                break
            except TargetNotFoundError:
                fail_times += 1


        if fail_times == 3:
            print("登录失败")
        else:
            print("登录成功")

    def change_player(self):
        touch(self.change_player_button_template)

    def main(self):
        self.start_app()


if __name__ == '__main__':
    aa = DownloadPage()
    aa.download()
    # aa.base_stop()