# encoding=utf8
import urllib
import socket
import requests
import bs4
import urllib.request
import urllib.parse
from urllib.request import urlopen
from tools import get_html

socket.setdefaulttimeout(3)
f = open("./proxy.txt")
lines = f.readlines()
proxys = []
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
for i in range(1, len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://" + ip[0] + ":" + ip[1]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
# url = "http://httpbin.org/ip"
url = "http://ip.chinaz.com/"
proxy = {'http:': 'http://118.187.58.34:53281'}
res = requests.get(url, proxies=proxy).text
bsobj = bs4.BeautifulSoup(res, 'html.parser')
temp = bsobj.find('input', attrs={'id': 'address'})["value"]
print(temp)
"""for proxy in proxys:
    try:
        # res = urlopen(url, proxies=proxy).read()
        # res = requests.get(url, proxies="http:":"http://218.75.158.153:3128").text
        res = requests.get(url, headers=headers, proxies="http:":"http://218.75.158.153:3128").text
        bsobj = bs4.BeautifulSoup(res, 'html.parser')
        temp = bsobj.find('input', attrs={'id': 'address'}).find('value')
        print(temp)
    except Exception as e:
        # print(proxy)
        print(e)
        continue"""
