from threading import Thread
from datetime import datetime, timedelta
from keywords import feed_page
import time
import os
from utils.email_sender import sender
from airtest.core.api import *


def task1():
    print(os.getcwd())
    feed = feed_page.FeedPage()
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


if __name__ == '__main__':
    feed_page.FeedPage().base_stop()
    t1 = Thread(target=task1)
    t1.start()
    # feed_thread = Thread(target=feed_page.FeedPage().main())
