import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


# 天气后报 查找所有城市名
def reptile_tqhb_city():
    url = 'http://tianqihoubao.com/lishi'
    response = requests.get(url=url)
    response.encoding = response.apparent_encoding
    html = response.text
    soup = bs(html, 'lxml')  # 页面源码
    table = soup.find_all(class_='citychk')  # 查找table标签
    # print(table)
    # 遍历每个标签，提取标签内容
    text = ''
    city_cn = []
    for tag in table:
        # 提取<a>标签内容
        a_tags = tag.find_all('a', limit=None)
        for a_tag in a_tags:
            if not a_tag.find('b'):  # 提取没有<b>标签的内容
                text += str(a_tag)
                city_cn.append(a_tag.text.strip(' '))
    # 正则匹配
    pattern = r'href="/lishi/(\w+)\.html"'
    city_py = re.findall(pattern, text)
    # 输出结果
    print(city_cn)
    print(city_py)
    # 将数据转换成DataFrame格式
    df = pd.DataFrame({'City_CN': city_cn, 'City_PinYin': city_py})
    # 写入Excel
    file = '../../resource/file/tqhb.xlsx'
    df.to_excel(file, index=False)  # index False为不写入索引
    print('天气后报 数据写入成功！')
    return


# 天气史 查找所有城市拼音
def reptile_tqs_city():
    url = 'https://www.tianqishi.com/lishi/'
    response = requests.get(url=url)
    response.encoding = response.apparent_encoding
    html = response.text
    soup = bs(html, 'lxml')  # 页面源码
    table = soup.find_all(class_='hd')  # 查找clss为hd的标签
    # print(table)
    # 遍历每个标签，提取标签内容
    text = ''
    city_cn = []
    for tag in table:
        # 提取<a>标签内容
        a_tags = tag.find_all('a', limit=None)
        for a_tag in a_tags:
            if not a_tag.find('b'):  # 提取没有<b>标签的内容
                text += str(a_tag)
                city_cn.append(a_tag.text.strip(' '))
    # 正则匹配
    pattern = r'href="/lishi/(\w+)\.html"'
    city_py = re.findall(pattern, text)
    del city_cn[0:2]
    print(city_cn)
    print(city_py)

    # 将数据转换成DataFrame格式
    df = pd.DataFrame({'City_CN': city_cn, 'City_PinYin': city_py})
    # 写入Excel
    file = '../../resource/file/tqs.xlsx'
    df.to_excel(file, index=False)  # index False为不写入索引
    print('天气史 数据写入成功！')
    return


# if __name__ == '__main__':
#     reptile_tqhb_city()
#     reptile_tqs_city()
