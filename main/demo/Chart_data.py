import requests
from bs4 import BeautifulSoup as bs
from ttkbootstrap.constants import *

import API
import Component
import Tran_pinyin


# 爬取天气后报数据  旭日图
def pre_data_tqhb():
    # 自动定位获取城市编码
    loc = API.location_query()
    # 城市中文名
    city_CN = loc['city0']
    # 上个月年月值
    date = str(int(Component.get_now_ym()) - 1)
    city_PY = Tran_pinyin.find_tqhb_py(city_CN)
    url = 'http://tianqihoubao.com/lishi/' + city_PY + '/month/' + date + '.html'
    try:
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
        # data = []
    except:
        data = []
        print('旭日图和雷达图数据异常')
    # print(data)
    return data


# 获取数据集  旭日图
tqhb_data = pre_data_tqhb()


# 旭日图数据
def data_pie():
    result = [tuple(tqhb_data[i + 1].split('/')) for i in range(0, len(tqhb_data), 4)]
    try:
        del result[0]
    except:
        result = []
    # 白天： 晴天 雨雪 多云/阴天 其他
    day_sunny = 0
    day_rain_snow = 0
    day_cloud = 0
    day_other = 0
    for x in result:
        if x[0] == '晴':
            day_sunny += 1
        elif '雨' in x[0] or '雪' in x[0]:
            day_rain_snow += 1
        elif x[0] == '多云' or x[0] == '阴':
            day_cloud += 1
        else:
            day_other += 1

    # 夜晚：晴天 雨雪 多云/阴 其他
    night_sunny = 0
    night_rain_snow = 0
    night_cloud = 0
    night_other = 0
    for x in result:
        if x[1] == '晴':
            night_sunny += 1
        elif '雨' in x[1] or '雪' in x[1]:
            night_rain_snow += 1
        elif x[1] == '多云' or x[1] == '阴':
            night_cloud += 1
        else:
            night_other += 1

    count = {'x1': [day_sunny + night_sunny, day_rain_snow + night_rain_snow, day_cloud + night_cloud,
                    day_other + night_other],
             'x2': [day_sunny, night_sunny, day_rain_snow, night_rain_snow, day_cloud, night_cloud, day_other,
                    night_other]}
    return count


# 爬取天气史数据 雷达图、折线图数据
def pre_data_tqs():
    # 自动定位获取城市编码
    loc = API.location_query()
    # 城市中文名
    city_CN = loc['city0']
    city_py = Tran_pinyin.find_tqs_py(city_CN)
    # print(city_py)
    # 爬取数据
    url = 'https://www.tianqishi.com/lishi/' + city_py + '.html'
    data = []
    try:
        response = requests.get(url=url)
        html = response.text
        soup = bs(html, 'lxml')  # 页面源码
        table = soup.find(class_='yuBaoTable')  # 查找table标签
        # 查找前30条记录
        for i in range(30):
            body_tr = table.find_all('tr')[i].text.replace(' ', '').replace('\n', ' ').replace('℃', '').split(
                ' ')  # 查找行
            tr_list = []
            for item in body_tr:
                if item != '':
                    tr_list.append(item)
            data.append(tr_list)
        # data = []
    except:
        data = []
    finally:
        data.reverse()
        return data


# 天气史 折线图数据
tqs_data = pre_data_tqs()


# 雷达图数据
def data_polar():
    # 折线图数据
    wind = []
    for j in tqs_data:
        # 防止数据没更新
        try:
            # 为了各数据的列表长度一样
            wind.append(j[3].split('风')[0])
        except:
            continue
    # 白天
    day_e = wind.count('东')
    day_s = wind.count('南')
    day_w = wind.count('西')
    day_n = wind.count('北')
    day_es = wind.count('东南')
    day_sw = wind.count('西南')
    day_wn = wind.count('西北')
    day_en = wind.count('东北')
    result = {"北": day_n, "西北": day_wn, "西": day_w, "西南": day_sw, "南": day_s, "东南": day_es, "东": day_e,
              "东北": day_en}
    return result


# 折线图数据
def data_line():
    tem_data = []
    high_tem = []
    low_tem = []
    for j in tqs_data:
        # 防止数据没更新不能转成int类型
        try:
            # 为了各数据的列表长度一样
            low_tem.append(int(j[1].split('~')[0]))
            # 防止出现空字符
            high_tem.append(int(j[1].split('~')[1]))
            # 转换类型去掉前面的0
            tem_data.append(str(int(j[0][6:])))
        except:
            continue
    result = {'日期': tem_data, '最高温度': high_tem, '最低温度': low_tem}
    # print(len(tem_data), len(high_tem), len(low_tem))
    return result


# 天气史
# 获取最高温度
def pre_data_bar():
    # 数据
    city_list0 = ['北\n京', '上\n海', '天\n津', '重\n庆', '哈\n尔\n滨', '长\n春', '沈\n阳', '呼\n和\n浩\n特',
                  '石\n家\n庄',
                  '太\n原', '西\n安',
                  '济\n南', '乌\n鲁\n木\n齐', '拉\n萨', '西\n宁', '银\n川', '银\n川', '南\n京', '武\n汉', '杭\n州',
                  '合\n肥',
                  '福\n州', '南\n昌', '长\n沙', '贵\n阳', '成\n都', '广\n州', '昆\n明', '南\n宁', '海\n口', '香\n港',
                  '澳\n门',
                  '台\n北']
    city_list = city_list0
    city_l = []
    for i in city_list:
        city = i.replace('\n', '')
        city_l.append(city)

    data = []
    # 查找拼音
    for city_CN in city_l:
        # 查找
        result = Tran_pinyin.find_tqs_py(city_CN)
        data.append(result)
    tem_list = []
    # 爬取数据
    for city in data:
        # 防止被封禁
        try:
            url = 'https://www.tianqishi.com/lishi/' + city + '.html'
            # print(url)
            response = requests.get(url=url, params={'param': '1'}, headers={'Connection': 'close'})
            html = response.text
            # print(html)
            soup = bs(html, 'lxml')  # 页面源码
            table = soup.find_all('table')[1]  # 查找table标签
            # print(table)
            tr_tag = table.find_all('tr')[0]  # 查找tr标签
            td_tag = tr_tag.find_all('td')[1].text  # 查找td标签
            hot_tem = td_tag.strip('℃').split('~')[1]  # 查找最高温度
            # print(hot_tem)
            # 防止被封
            # if len(tem_list) == 10:
            #     time.sleep(1)
            # 防止网站数据没更新而爬到空数据
            # if hot_tem == '':
            #     tem_list.append(0)
            # else:
            tem_list.append(int(hot_tem))
        # 获取异常
        except:
            # 防止异常
            tem_list.append(0)
        finally:
            continue
    return {'城市': city_list, '数据': tem_list}


# 天气史 获取各城市数据集
bar_data = pre_data_bar()


# 条形图数据
def data_bar():
    return bar_data


# 表格数据
def data_table(hot_title_label, hot_update_label, hot_box, cold_title_label, cold_update_label, cold_box):
    # 爬取数据
    def get_data(url):
        response = requests.get(url)
        html = response.text
        # print(html)
        soup = bs(html, 'lxml')  # 页面源码
        # print(soup)
        # 查找标题
        title = soup.find_all('h1')[0].text.split('-')[1]
        # print(title)
        # 查找更新时间
        update = soup.find(class_='j-temp-tips').text
        # print(update)
        # 查找表格元素
        table = soup.find(class_='j-table')
        tbody = table.find(class_='j-tbody')  # 查找表格内容
        data = []
        for i in range(100):
            body_tr = tbody.find_all(class_='j-tr')[i].text.replace(' ', '').replace('\n', ' ').split(' ')  # 查找行
            tr_list = []
            for item in body_tr:
                if item != '':
                    tr_list.append(item)
            data.append(tr_list)
        result = {'标题': title, '更新时间': update, '数据': data}
        return result

    try:
        # 最高气温数据写入
        url_hot = 'https://tianqi.2345.com/temperature-rank.htm'
        hot_data = get_data(url_hot)
        hot_title_label.configure(text=hot_data['标题'])
        hot_update_label.configure(text=hot_data['更新时间'])
        for row1 in hot_data['数据']:
            hot_box.insert('', END, values=row1)
        # 最低气温数据写入
        url_cold = 'https://tianqi.2345.com/temperature-rank-rev.htm'
        cold_data = get_data(url_cold)
        cold_title_label.configure(text=cold_data['标题'])
        cold_update_label.configure(text=cold_data['更新时间'])
        for row2 in cold_data['数据']:
            cold_box.insert('', END, values=row2)
    except:
        return

# print(data_pie())
# print(data_polar())
# print(data_line())
# print(data_bar())
# print(data_table())
