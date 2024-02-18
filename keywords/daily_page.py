from feed_page import FeedPage
from datetime import datetime, timedelta
from airtest.core.api import *
from utils.email_sender import sender


class DailyPage:

    # 寄养
    def task1(self):
        feed = FeedPage()
        while True:
            try:
                now = datetime.now()
                last_time = feed.base_search('feed_time', {'phone': '18576265815'})['msg']['last_time']
                if (now - timedelta(hours=6)) > last_time:
                    print("寄养时间到，开始蹲坑")
                    feed.main()
                else:
                    # print("未到寄养时间，还剩", last_time - (now - timedelta(hours=6)))
                    time.sleep(60)
            except Exception as e:
                snapshot(filename='log\\unknown\\error.png')
                sender('未知错误', pic_path='log\\unknown\\error.png', text=f'{e}\n遇到未知错误，请人工介入')

    # 业原火+突破刷勾玉
    def task2(self):
        pass


    # 地域鬼王
    def task3(self):
        pass

    # 麒麟
    def task4(self):
        pass

    # 阴界之门
    def task5(self):
        pass

    # 峡间
    def task6(self):
        pass

    # 道馆
    def task7(self):
        pass

    # 宴会
    def task8(self):
        pass

    # 点逢魔
    def task9(self):
        pass

    # 打封魔
    def task10(self):
        pass