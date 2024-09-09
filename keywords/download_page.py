from airtest.core.api import *
from base_page import BasePage
import os


class DownloadPage(BasePage):
    click_to_start_button_template = Template(r'static/app/登录界面/进入游戏.png')
    # change_player_button_template = Template()
    desktop_icon = Template(r'static/desktop/桌面图标.png')
    age_icon = Template(r'static/app/登录界面/用于判断登录界面.png')

    advertisement_close_button = Template(r'static/app/庭院/关闭广告.png')
    juanzhou_button_template = Template(r'static/app/庭院/庭院卷轴.png')

    # 随便放一张
    update_button = Template('static/app/庭院/庭院卷轴.png')

    user_center_button = Template('static/app/登录界面/用户中心.png')
    exchange_user_button = Template('static/app/登录界面/切换账号.png')
    checkbox_button = Template('static/app/登录界面/下拉框.png')
    download_button = Template('static/app/登录界面/登录按钮.png')
    ios_button = Template('static/app/登录界面/ios平台.png')
    android_button = Template('static/app/登录界面/安卓平台.png')
    exchange_server_button = Template('static/app/登录界面/换区按钮.png')

    # 角色位置预留

    # 服务器位置预留


    def download(self,user,platform):
        self.base_start()
        print(os.getcwd())
        sleep(15)
        for i in range(3):
            sleep(3)
            touch((100, 100))
            sleep(3)
            touch((100, 100))

            self.update_app()

            try:
                if wait(self.age_icon):
                    print("进入登录界面成功")
                    sleep(7)
                    self.change_player(user,platform)
                    sleep(2)
                    touch(self.click_to_start_button_template)
                    print("进入游戏成功")
                    break

            except TargetNotFoundError:
                print("没找到进入游戏按钮")

            sleep(20)
            for i in range(10):
                if exists(self.advertisement_close_button):
                    touch(self.advertisement_close_button)
                else:
                    break
            # 成功进入庭院
            if exists(self.juanzhou_button_template):
                print("成功进入庭院")

    def change_player(self, user, platform):
        # 点击用户中心
        touch(self.user_center_button)
        sleep(2)
        # 点击切换账号
        if exists(self.exchange_user_button):
            touch(self.exchange_user_button)
        sleep(2)
        # 点击下拉框
        touch((961, 507))
        sleep(2)
        # 选择账号预留
        path = f'static/user/{user}.png'
        touch(Template(path))
        sleep(2)

        # 点击登录
        touch(self.download_button)

        # 选择账号相应平台
        if platform =="ios":
            touch(self.ios_button)
        else:
            touch(self.android_button)
        sleep(2)

        # 选择账号相应区服
        touch(self.exchange_server_button)
        sleep(2)

        # touch((1126, 788))
        touch((464, 883))
        sleep(2)

        touch((459, 769))
        sleep(2)

    def update_app(self):
        if exists(self.update_button):
            touch(self.update_button)
            sleep(180)
            print("需要更新")

    def exchange_user(self, user):

        pass

    def main(self,user,platform):
        self.download(user,platform)


    def test(self):
        # for i in range(10):
        #     if exists(self.advertisement_close_button):
        #         print("找到广告")
        #         touch(self.advertisement_close_button)
        #     else:
        #         print("没找到，跳出")
        #         break
        # # 成功进入庭院
        # if exists(self.juanzhou_button_template):
        #     print("成功进入庭院")
        # else:
        #     print("进入庭院失败")
        self.change_player("18576265815","ios")

if __name__ == '__main__':
    import os
    print(os.getcwd())
    aa = DownloadPage()
    aa.base_conncet()
    aa.test()
    # aa.base_stop()
