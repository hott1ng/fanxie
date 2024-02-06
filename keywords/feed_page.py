from base_page import BasePage
from airtest.core.api import *
from control.mymongo import MongoMoudle
from datetime import datetime
from utils.sender import qq_send
from download_page import DownloadPage


class FeedPage:
    yinyangliao_button_template = Template(r'../static/app/阴阳寮.png')
    jiejie_button_template = Template(r'../static/app/结界.png')
    shishenyucheng_button_template = Template(r'../static/app/结界图标/式神育成.png')

    six_taigu_template = Template(r'../static/app/结界图标/六星太鼓.png')
    five_taigu_template = Template(r'../static/app/结界图标/五星太鼓.png')
    six_douyu_template = Template(r'../static/app/结界图标/六星斗鱼.png')
    # five_douyu_template = Template()

    friend_button_template = Template(r'../static/app/结界图标/好友.png')
    kuaqu_button_template = Template(r'../static/app/结界图标/跨区.png')

    enter_jiejie_button_template = Template(r'../static/app/结界图标/进入结界.png')
    feed_button_template = Template(r'../static/app/结界图标/去寄养.png')

    feed_boy_template = Template(r'../static/app/结界图标/寄养专用.png')

    ok_button_template = Template(r'../static/app/结界图标/确定.png')

    juanzhou_template = Template(r'../static/app/庭院卷轴.png')




    def __int__(self):
        self.mongo =  MongoMoudle()


        pass

    # def goto_feed(self):
    #     touch(self.shenshe_button_template)
    #
    #     touch(self.jiejie_button_template)

    def feed(self):
        priority_pool = {
            0: self.six_taigu_template,
            1: self.five_taigu_template,
            2: self.six_douyu_template,
            # 3: self.five_douyu_template
        }

        touch(self.shishenyucheng_button_template)
        touch(self.feed_button_template)

        # ok







        result = []
        # 查询坑位
        touch(self.kuaqu_button_template)
        sleep(2)
        try:
            for i in range(4):
                kuaqu_result = [dict(j, version=1, priority=i) for j in find_all(priority_pool[i])]
                result.extend(kuaqu_result)
        except:
            print('跨区无坑位')
        touch(self.friend_button_template)
        sleep(2)
        try:

            for i in range(4):
                benfu_result = [dict(j, version=0, priority=i) for j in find_all(priority_pool[i])]
                result.extend(benfu_result)
        except:
            print('本服无坑位')

        result = sorted(result, key=lambda x: x['priority'])
        print(result)
        touch(result[0]['result'])
        print('点击',result[0]['result'])
        touch(self.enter_jiejie_button_template)



        # 点击加号
        touch(self.feed_button_template)

        # 选择寄养专属
        touch(self.feed_boy_template)

        # 点击确定
        touch(self.ok_button_template)

        # self.commit()

        # self.back()

    def commit(self):
        pass
        date = datetime.now()

        if self.mongo.search(username):
            self.mongo.update(username, date)

        else:
            self.mongo.insert(username, date)


    def back(self):
        pass


    def main(self):
        # 启动



        # 从庭院出发
        touch(self.juanzhou_template)

        # 点击阴阳寮
        touch(self.yinyangliao_button_template)

        # 点击结界
        touch(self.jiejie_button_template)

        # 寄养流程
        self.feed()

        # 退出应用
        sleep(3)

if __name__ == '__main__':
    connect_device("Android:///")

    device = device()
    aa = FeedPage()
    aa.main()