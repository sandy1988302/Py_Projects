import requests
import os

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'
}
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '30',
}
response = requests.get(url=url, params=params, headers=headers)

# .json()表示将获取的字符串形式的json数据序列化成字典或者列表
page_text = response.json()

# 解析出电影的名称和评分
for movie in page_text:
    movie_name = movie['title']
    movie_socre = movie['score']
    print(movie_name, movie_socre)
