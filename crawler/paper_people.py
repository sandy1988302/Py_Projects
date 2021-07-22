import bs4
import os
import time
from tools import get_days
from tools import get_html


def get_page_list(y, m, d):
    """
    功能：获取当天报纸的各版面的链接列表
    参数：年，月，日
    """
    url = 'http://paper.people.com.cn/rmrb/html/' + y + '-' + m + '/' + d + '/nbs.D110000renmrb_01.htm'
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    temp = bsobj.find('div', attrs={'id': 'page_list'})
    if temp:
        page_list = temp.ul.find_all('div', attrs={'class': 'right_title-name'})
    else:
        page_list = bsobj.find('div', attrs={'class': 'swiper-container'}). \
            find_all('div', attrs={'class': 'swiper-slide'})
    link_list = []
    for page in page_list:
        link = page.a["href"]
        url = 'http://paper.people.com.cn/rmrb/html/' + y + '-' + m + '/' + d + '/' + link
        link_list.append(url)

    return link_list


def get_title_list(y, m, d, page_url):
    """
    功能：获取报纸某一版面的文章链接列表
    参数：年，月，日，该版面的链接
    """
    html = get_html.fetch_url(page_url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    temp = bsobj.find('div', attrs={'id': 'title_list'})
    if temp:
        title_list = temp.ul.find_all('li')
    else:
        title_list = bsobj.find('ul', attrs={'class': 'news-list'}).find_all('li')

    link_list = []
    for title in title_list:
        temp_list = title.find_all('a')
        for temp in temp_list:
            link = temp["href"]
            if 'nw.D110000renmrb' in link:
                url = 'http://paper.people.com.cn/rmrb/html/' + y + '-' + m + '/' + d + '/' + link
                link_list.append(url)
    return link_list


def get_content(html):
    """
    功能：解析 HTML 网页，获取新闻的文章内容
    参数：html 网页内容
    """
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    # 获取文章 标题
    title = bsobj.h3.text + '\n' + bsobj.h1.text + '\n' + bsobj.h2.text + '\n'
    # print(title)
    # 获取文章 内容
    p_list = bsobj.find('div', attrs={'id': 'ozoom'}).find_all('p')
    content = ''
    for p in p_list:
        content += p.text + '\n'
        # print(content)
    # 返回结果 标题+内容
    resp = title + content
    return resp


def save_file(content, path, filename):
    """
    功能：将文章内容 content 保存到本地文件中
    参数：要保存的内容，路径，文件名
    """
    # 如果没有该文件夹，则自动生成
    if not os.path.exists(path):
        os.makedirs(path)
    # 保存文件
    with open(path + filename, 'w', encoding='utf-8') as f:
        f.write(content)


def download_rmrb(y, m, d, download_dir):
    """
    功能：爬取《人民日报》网站 某年 某月 某日 的新闻内容，并保存在 本文件同级的data目录下
    参数：年，月，日，文件保存的根目录
    """
    page_list = get_page_list(y, m, d)
    for page in page_list:
        title_list = get_title_list(y, m, d, page)
        for url in title_list:
            # 获取新闻文章内容
            html = get_html.fetch_url(url)
            content = get_content(html)
            # 生成保存的文件路径及文件名
            temp = url.split('_')[2].split('.')[0].split('-')
            page_no = temp[1]
            title_no = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
            path = download_dir + '/' + y + m + d + '/'
            file_name = y + m + d + '-' + page_no + '-' + title_no + '.txt'
            # 保存文件
            save_file(content, path, file_name)


if __name__ == '__main__':
    '''
    主函数：程序入口
    '''
    # 输入起止日期，爬取之间的新闻
    beginDate = input('请输入开始日期:')
    endDate = input('请输入结束日期:')
    data = get_days.get_date_list(beginDate, endDate)  # 获取开始日期和结束日期之间的日期列表

    for da in data:
        year = str(da.year)
        month = str(da.month) if da.month >= 10 else '0' + str(da.month)
        da = str(da.day) if da.day >= 10 else '0' + str(da.day)
        download_rmrb(year, month, da, 'data')  # date是目录名称
        print("爬取完成：" + year + month + da)
        time.sleep(3)  # 怕被封 IP 爬一爬缓一缓，爬的少的话可以注释掉
