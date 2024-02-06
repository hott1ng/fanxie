from threading import Thread
from datetime import datetime, timedelta
from keywords import feed_page
import time
from utils.email_sender import sender


def task1():
    feed = feed_page.FeedPage()
    while True:
        now = datetime.now()
        last_time = feed.base_search('feed_time', {'phone': '18576265815'})['msg']['last_time']
        if (now - timedelta(hours=6)) > last_time:
            print("寄养时间到，开始蹲坑")
            feed.main()
        else:
            time.sleep(60)


if __name__ == '__main__':
    t1 = Thread(target=task1)
    t1.start()
    # feed_thread = Thread(target=feed_page.FeedPage().main())
