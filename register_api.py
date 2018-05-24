#!usr/bin/python
# encoding:utf-8
# author:masako
# date:2018/05/24

import re
import json
import time
import requests


def check_phone(phone):
    """
    :param phone:
    :return: {
        "msg": error massage
        "code": return code
    }
    code:
    100000 - ok
    600001 - 该手机号已注册
    """
    t = time.time()
    timestamp = int(round(t * 1000))
    url = "https://weibo.com/signup/v5/formcheck?type=mobilesea&zone=0086&value=%s&from=&__rnd=%s" % (phone, timestamp)
    headers = {
        "Host": "weibo.com",
        "Referer": "https://weibo.com/signup/signup.php?lang=zh-cn&inviteCode=&from=&appsrc=&backurl=&showlogo=",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    result = {}
    try:
        response = requests.get(url, headers=headers, timeout=3)
    except Exception as e:
        result['msg'] = str(e)
        return result

    print response.content
    try:
        jsn = json.loads(response.content)
        data = jsn['data']
    except Exception as e:
        result['msg'] = str(e)
        return result

    result['code'] = data.get('code', '')
    msg = data.get('msg', '')
    msg_ch = re.sub('<.*?>', '', msg)
    result['msg'] = msg_ch
    return result


def register(phone, sms):
    pass


if __name__ == "__main__":
    print check_phone('18482396637')

