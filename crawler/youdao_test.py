# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import time
import random
import hashlib
import json

'''使用urlopen(request_url,data)发送参数'''

if __name__ == "__main__":
    # 对应上图的Request URL
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    header = {
        "Accept": " application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": " XMLHttpRequest",
        "User-Agent": " Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": " zh-CN,zh;q=0.9"
    }
    i = input("Translation for: ")
    u = 'fanyideskweb'
    d = i
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = 'ebSeFb%=XZ%T[KZ)c(sy!'
    md5 = hashlib.md5()
    md5.update(u.encode('utf-8'))
    md5.update(d.encode('utf-8'))
    md5.update(f.encode('utf-8'))
    md5.update(c.encode('utf-8'))
    sign = md5.hexdigest()
    data = {
        "i": i,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": f,
        "sign": sign,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    request_url = request.Request(url, data=data, headers=header)
    response = request.urlopen(request_url)
    # 如果200，获取response成功
    print(response.getcode())
    # 读取信息并解码, 转化为json格式
    json_result = json.loads(response)
    translation_result = json_result['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translation_result)
