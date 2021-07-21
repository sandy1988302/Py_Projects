# encoding=utf8
import requests
import bs4

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {'User-Agent': User_Agent}

url = 'http://www.66ip.cn/areaindex_18/1.html'
req = requests.get(url, headers=header)
req.raise_for_status()
req.encoding = req.apparent_encoding

soup = bs4.BeautifulSoup(req.text, 'html.parser')
ips = soup.findAll('tr')
# f = open("./proxy.txt", "w")


for x in range(1, len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[0].contents[0] + "\t" + tds[1].contents[0] + "\n"
    print(ip_temp)
    #f.write(ip_temp)
