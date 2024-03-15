import requests
import base64
import hashlib


def wechat_send(path,text):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6f50d05c-fde2-4539-941d-8288546dca5c"
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
        data['text']['content']['mentioned_list'] = ['yufeifan']


    response = requests.post(url, json=data)

# wechat_send('','成功')