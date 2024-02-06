import os
from airtest.core.api import *




def StartClient():
    os.system("adb connect 127.0.0.1:7555")
    return connect_device("Android:///")


print(StartClient())