import Tran_pinyin
from Component import *


# 数据来自 天气后报
# 爬取历史天气数据
def weather_reptile(city_CN, date, box):
    try:
        city_PY = Tran_pinyin.find_tqhb_py(city_CN)
        url = 'http://tianqihoubao.com/lishi/' + city_PY + '/month/' + date + '.html'
        response = requests.get(url=url)
        response.encoding = response.apparent_encoding
        html = response.text
        soup = bs(html, 'lxml')  # 页面源码
        table = soup.find_all('table')[0]  # 查找table标签
        # 数据处理
        data = []
        td_list = table.find_all('td')
        for i in td_list:
            weather = str(i.text).replace('\n', '').replace('\r', '').replace(' ', '')
            data.append(weather)
        result = [(city_CN, data[i], data[i + 1], data[i + 2], data[i + 3]) for i in range(0, len(data), 4)]
        result.remove(result[0])  # 去掉第一组数据
        # 写入
        for row in result:
            box.insert('', END, values=row)
        return result
    except:
        return


# 历史天气 开启线程
# def history_thread(city_CN, date, box):
#     # 开启线程
#     t1 = threading.Thread(target=weather_reptile, args=(city_CN, date, box))
#     t1.start()


# 爬取本市历史天气
def weather_r(city_CN, date):
    try:
        city_PY = Tran_pinyin.find_tqhb_py(city_CN)
        url = 'http://tianqihoubao.com/lishi/' + city_PY + '/month/' + date + '.html'
        response = requests.get(url=url)
        response.encoding = response.apparent_encoding
        html = response.text
        soup = bs(html, 'lxml')  # 页面源码
        table = soup.find_all('table')[0]  # 查找table标签
        # 数据处理
        data = []
        td_list = table.find_all('td')
        for i in td_list:
            weather = str(i.text).replace('\n', '').replace('\r', '').replace(' ', '')
            data.append(weather)
        result = [(city_CN, data[i], data[i + 1], data[i + 2], data[i + 3]) for i in range(0, len(data), 4)]
        result.remove(result[0])  # 去掉第一组数据
        return result
    except:
        return


# if __name__ == '__main__':
#     reptile_data = weather_reptile('北京', '202003')
#     print(reptile_data)
