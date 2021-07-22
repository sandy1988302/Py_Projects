# -*- coding: UTF-8 -*-

from urllib import request
import chardet
import urllib.parse

if __name__ == "__main__":
    # request_url = request.Request("https://www.csdn.net/")
    # response = request.urlopen(request_url)
    # html = response.read()
    # encoding = chardet.detect(html)['encoding']
    # html = html.decode(str(encoding))  # 从默认使用的Unicode 转为网页的utf-8
    # print(html)

    url = 'https://so.csdn.net/so/search/s.do'
    params = {'q': 'Dr.CH起不来', }
    header = {
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                      "91.0.4472.124 Safari/537.36",
    }
    # 使用parse方法对参数进行URL编码
    encoded_params = urllib.parse.urlencode(params)
    # 拼装后的request地址是https://so.csdn.net/so/search/s.do?q=Dr.CH起不来
    request_url = urllib.request.Request(url + '?' + encoded_params, headers=header)
    response = urllib.request.urlopen(request_url)
    html = response.read()
    encoding = chardet.detect(html)['encoding']  # 获取网页的编码（utf-8）
    print(html.decode(str(encoding)))
