# encoding=utf8
import urllib
import socket
import requests
import bs4
import urllib.request
import urllib.parse
from urllib.request import urlopen

socket.setdefaulttimeout(3)
f = open("./proxy.txt")
lines = f.readlines()
proxys = []
for i in range(0, len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://" + ip[0] + ":" + ip[1]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
url = "http://httpbin.org/ip"
for proxy in proxys:
    try:
        #res = urlopen(url, proxies=proxy).read()
        res = requests.get(url, proxies=proxy).text
        print(res)
    except Exception as e:
        print(proxy)
        print(e)
        continue
