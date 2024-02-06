from airtest.core.api import *
import os

class BasePage(object):
    def __init__(self):
        # adb连接设备
        # os.system('adb conncet 127.0.0.1:7555')
        # airtest连接设备
        connect_device("Android:///")

    def base_start(self):
        shell('am start com.netease.onmyoji.wyzymnqsd_cps/com.netease.onmyoji.tag0')


    def base_stop(self):
        shell('am force-stop com.netease.onmyoji.wyzymnqsd_cps')


if __name__ == '__main__':
    BasePage().base_start()