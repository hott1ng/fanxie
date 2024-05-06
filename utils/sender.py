import requests
import base64
import hashlib


def wechat_send(path,text):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a8145c62-e234-403c-8517-42f5021b7378"
    with open(path, 'rb') as f:
    # with open(r'D:\project202402\fanxie\log\screenshot\寄养结果2024_03_14_10_01_47.png', 'rb') as f:
        img = f.read()
    md5 = hashlib.md5(img).hexdigest()

    data = {
        "msgtype": "image",
        "image": {
            "base64": base64.b64encode(img).decode("ascii"),
            "md5": md5
        }
    }





    response = requests.post(url, json=data)

    data = {
    "msgtype": "text",
    "text": {
        "content": text,
        # "mentioned_list":["wangqing","@all"],
        # "mentioned_mobile_list":["13800001111","@all"]
    }
}

    if '请' in text:
        data['text']['mentioned_list'] = ['yufeifan']


    response = requests.post(url, json=data)

