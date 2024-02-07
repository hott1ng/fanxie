from airtest.core.api import *
from control.mymongo import MongoMoudle

import os


class BasePage(object):

    def base_start(self):
        # adb连接设备
        os.system('adb connect 127.0.0.1:7555')
        # airtest连接设备
        connect_device("Android:///")
        # 开启前先关闭
        shell('am force-stop com.netease.onmyoji.wyzymnqsd_cps')

        shell('am start com.netease.onmyoji.wyzymnqsd_cps/com.netease.onmyoji.tag0')

    def base_stop(self):
        # adb连接设备
        os.system('adb connect 127.0.0.1:7555')
        # airtest连接设备
        connect_device("Android:///")
        shell('am force-stop com.netease.onmyoji.wyzymnqsd_cps')

    def base_conncet(self):
        os.system('adb connect 127.0.0.1:7555')
        # airtest连接设备
        connect_device("Android:///")

    def base_insert(self, table, data):
        return MongoMoudle().insert(table, data)

    def base_update(self, table, select, data):
        return MongoMoudle().update(table, select, data)

    def base_search(self, table, data):
        return MongoMoudle().search(table, data)


if __name__ == '__main__':
    BasePage().base_start()
