import threading
import time

import pandas as pd
import requests
from ttkbootstrap.constants import *
from bs4 import BeautifulSoup as bs
import ttkbootstrap as ttkbs

import API
import Reptile


# 动态更新时间 组件
def now_time():
    time_str1 = time.strftime('%Y年%m月%d日 %H:%M', time.localtime())  # 获取时间
    TimeNow = ttkbs.Label(text=time_str1, background='', font=('黑体', 12))
    TimeNow.place(width=300, height=50, x=710, y=40)
    TimeNow.after(1000, now_time)  # 一秒刷新一次


# 获取当前年月
def get_now_ym():
    year_month = time.strftime('%Y%m', time.localtime())
    return year_month


# 获取日历框年月值
def get_box_ym(box):
    date = box.entry.get()
    d = date.split('-')
    result = d[0] + d[1]
    return result


# 获取日历框年月值
def get_box_day(box):
    date = box.entry.get()
    d = date.split('-')
    result = int(d[2])
    return result


# 获取搜索框的城市名
def get_box_city(box):
    city = box.get()
    if city == '请输入城市名' or city == '':
        # 自动定位
        loc = API.location_query()
        city0 = loc['city0']
        result = city0
        return result
    else:
        return city


# 根据年月和城市名获取历史天气数据
def get_history(date_box, city_box, box):
    try:
        date = get_box_ym(date_box)
        city = get_box_city(city_box)
        day = get_box_day(date_box)
        result = Reptile.weather_reptile(date=date, city_CN=city, box=box)
        # print(result)
        # 清空
        for row in box.get_children():
            box.delete(row)
        # 写入
        for i, row in enumerate(result):
            # print(i, row)
            id = box.insert('', END, values=row)
            if i + 1 == day:
                # print(row)
                # 设置选中状态
                box.selection_set(id)
            # print(row)
    except:
        pass


# 清空内容窗口
def box_clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# 搜索 开启线程
def search_thread(date_box, city_box, text_box):
    t2 = threading.Thread(target=get_history, args=(date_box, city_box, text_box))
    t2.start()


# 日出日落content_box
def sun_updown():
    try:
        # 查找日出日落
        url = 'https://tianqi.2345.com/'
        response = requests.get(url=url)
        response.encoding = response.apparent_encoding
        html = response.text
        soup = bs(html, 'lxml')  # 页面源码
        # print(soup)
        # 日出
        sun_up_text = soup.find(class_='banner-whether-info1-l').text.strip('\n').split(' ')  # 查找日出时间
        sun_up = []
        for i in sun_up_text:
            if i != '':
                sun_up.append(i)
        # del sun_up[0]
        # 日落
        sun_down_text = soup.find(class_='banner-whether-info1-r').text.strip('\n').split(' ')  # 查找日落时间
        sun_down = []
        for i in sun_down_text:
            if i != '':
                sun_down.append(i)
        # del sun_down[0]
        result = {sun_up[0]: sun_up[1], sun_down[0]: sun_down[1]}
        return result
    except:
        pass


# 日出日落线程
# def sun_threading(content_box):
#     sun_th = threading.Thread(target=sun_updown, args=(content_box,))
#     sun_th.start()


# 开机自启
def auto_boot(var):
    # 获取offvalue和onvalue
    val = var.get()
    # print(val)
    file = '../resource/file/setting.csv'
    df = pd.read_csv(file)
    if val == 0:    # 关闭
        df['auto_boot'] = [0]
        df.to_csv(file, index=False)
    if val == 1:    # 打开
        df['auto_boot'] = [1]
        df.to_csv(file, index=False)


# 服务通知
def service_notice(var):
    # 获取offvalue和onvalue
    val = var.get()
    # print(val)
    file = '../resource/file/setting.csv'
    df = pd.read_csv(file)
    if val == 0:    # 关闭
        df['notice'] = [0]
        df.to_csv(file, index=False)
    if val == 1:    # 打开
        df['notice'] = [1]
        df.to_csv(file, index=False)


# 夜间模式
def theme_change(var):
    # 获取offvalue和onvalue
    val = var.get()
    # print(val)
    style = ttkbs.Style()
    file = '../resource/file/setting.csv'
    df = pd.read_csv(file)
    if val == 0:    # 关闭
        style.theme_use('cosmo')   # 日间模式
        df['dark'] = [0]
        df.to_csv(file, index=False)
    if val == 1:    # 打开
        style.theme_use('darkly')   # 夜间模式
        df['dark'] = [1]
        df.to_csv(file, index=False)


# 默认夜间或日间
def dark_default():
    file = '../resource/file/setting.csv'
    dt = pd.read_csv(file)
    val = dt['dark'].values[0]
    # print(val)
    style = ttkbs.Style()
    if val == 0:  # 关闭
        style.theme_use('cosmo')  # 日间模式
    if val == 1:  # 打开
        style.theme_use('darkly')  # 夜间模式 darkly


# 进度条
# def processbar():
#     progress_bar = ttkbs.Progressbar()
#     progress_bar.place(x=280, y=60, height=10, width=140)
