from threading import Thread
from datetime import datetime, timedelta
from keywords import feed_page
import time
import os
from utils.email_sender import sender
from airtest.core.api import *
from utils.sender import wechat_send


def task1():
    print(os.getcwd())
    feed = feed_page.FeedPage()
    while True:
        try:
            for i in ['18576265815',"haoge"]:
                now = datetime.now()
                data = feed.base_search('feed_time', {'phone': i})['msg']
                last_time = data['last_time']
                platform = data['platform']
                if (now - timedelta(hours=6)) > last_time:
                    if now.weekday() == 2 and 6 <= now.hour < 9:
                        time.sleep(60)
                    else:

                        print("寄养时间到，开始蹲坑")
                        feed.main(i, platform)
                # else:
                    # print("未到寄养时间，还剩", last_time - (now - timedelta(hours=6)))
            time.sleep(60)
        except Exception as e:
            snapshot(filename='log\\unknown\\error.png')
            time.sleep(1)
            wechat_send('log\\unknown\\error.png','遇到未知错误，请人工介入')


if __name__ == '__main__':
    feed_page.FeedPage().base_stop()
    t1 = Thread(target=task1)
    t1.start()
    # feed_thread = Thread(target=feed_page.FeedPage().main())