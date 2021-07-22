import re
from tools import get_html


if __name__ == "__main__":
    # 访问网址获取IP
    url = 'https://2021.ip138.com/'
    # 构建request对象
    html = get_html.fetch_url(url)
    pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')  # iP地址归属地查询
    ip_list = re.findall(pattern, html)
    print(ip_list[0])
