from tkinter import *

import Component
import Download_photo
import Photo_show
from Reptile import *

import Chart


# 自动定位
loc = API.location_query()
# 市
city0 = loc['city0']
# 区/县
city = loc['city']
# 城市编码
adcode = loc['adcode']
# 城市英文名
city_PY = Tran_pinyin.find_tqhb_py(city0)
# 高德地图API查询 live_picture
live_weath = API.live_weather(adcode=adcode)
# 高德地图API查询 预报天气
forecast_weath = API.forecast_weather(adcode=adcode)
# 心知天气API查询 各项指数
target = API.target(city=city_PY)
# 获取今天日期和该城市定位
year_month = Component.get_now_ym()  # 获取现在年月
data_history = weather_r(city_CN=city0, date=year_month)
# 获取日出日落
data_sun = Component.sun_updown()


# 今日天气
def today_weather(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 创建新窗口
    content_box = ttkbs.LabelFrame(master=frame, text='今日天气')
    content_box.place(width=700, height=550, x=0, y=0)
    # 分割线
    # ttkbs.Separator(master=content_box, orient=VERTICAL).place(width=1, height=380, x=200, y=80)
    # 城市名
    global loc_img
    loc_img = PhotoImage(file='../resource/image/定位.png').subsample(2, 2)
    loc_img_label = ttkbs.Label(master=content_box, background='', font=('黑体', 10), image=loc_img)
    loc_img_label.place(width=30, height=30, x=20, y=50)
    city_label = ttkbs.Label(master=content_box, text=city, background='', font=('黑体', 10))
    city_label.place(width=160, height=50, x=46, y=40)
    # 天气信息
    weather = live_weath['weather']
    # 图片
    global img
    if '雨' in weather:
        img = PhotoImage(file='../resource/image/雨天.png')
    else:
        img = PhotoImage(file='../resource/image/蓝天.png')
    img_label = Label(master=content_box, width=160, height=100, image=img)
    img_label.place(x=20, y=100)

    temperature = live_weath['temperature'] + '℃'
    humidity = '湿度 ' + live_weath['humidity'] + '%'
    wind = live_weath['winddirection'] + '风 ' + live_weath['windpower'] + '级'
    reporttime = '○ 更新时间 ' + str(live_weath['reporttime']).split()[1]
    weather_label = ttkbs.Label(master=content_box, text=weather, background='', font=('黑体', 18))
    weather_label.place(width=160, height=60, x=20, y=210)
    temperature_label = ttkbs.Label(master=content_box, text=temperature, background='', font=('黑体', 16))
    temperature_label.place(width=70, height=40, x=100, y=280)
    humidity_label = ttkbs.Label(master=content_box, text=humidity, background='', font=('黑体', 14))
    humidity_label.place(width=160, height=50, x=20, y=330)
    wind_label = ttkbs.Label(master=content_box, text=wind, background='', font=('黑体', 14))
    wind_label.place(width=160, height=50, x=20, y=380)
    reporttime_label = Label(master=content_box, text=reporttime)
    reporttime_label.place(width=160, height=50, x=20, y=440)
    global img_up
    global img_down
    img_up = PhotoImage(file='../resource/image/日出.png')
    img_down = PhotoImage(file='../resource/image/日落.png')
    Label(master=content_box, image=img_up).place(width=32, height=32, x=250, y=30)
    Label(master=content_box, image=img_down).place(width=32, height=32, x=380, y=30)
    # 图片
    global day_img1
    global night_img1
    day_img1 = PhotoImage(file='../resource/image/day80.png').subsample(2, 2)
    night_img1 = PhotoImage(file='../resource/image/night48.png')
    day_img_label1 = Label(master=content_box, image=day_img1)
    day_img_label1.place(width=80, height=80, x=220, y=90)
    night_img_label1 = Label(master=content_box, image=night_img1)
    night_img_label1.place(width=80, height=80, x=220, y=180)
    # 白天/夜晚 天气信息
    day_night = forecast_weath['casts'][0]
    day_weather = day_night['dayweather']
    night_weather = day_night['nightweather']
    day_temp = day_night['daytemp'] + '℃'
    night_temp = day_night['nighttemp'] + '℃'
    day_wind = day_night['daywind'] + '风'
    night_wind = day_night['nightwind'] + '风'
    day_power = day_night['daypower'] + '级'
    night_power = day_night['nightpower'] + '级'
    dayweather_label1 = Label(master=content_box, background='red', text=day_weather, font=('黑体', 16))
    dayweather_label1.place(width=120, height=40, x=300, y=90)
    nightweather_label1 = Label(master=content_box, background='red', text=night_weather, font=('黑体', 16))
    nightweather_label1.place(width=120, height=40, x=300, y=180)
    daytemp_label1 = Label(master=content_box, background='red', text=day_temp, font=('黑体', 14))
    daytemp_label1.place(width=80, height=40, x=350, y=130)
    nighttemp_label1 = Label(master=content_box, background='red', text=night_temp, font=('黑体', 14))
    nighttemp_label1.place(width=80, height=40, x=350, y=220)
    daywind_label1 = Label(master=content_box, background='red', text=day_wind, font=('黑体', 12))
    daywind_label1.place(width=80, height=40, x=460, y=110)
    nightwind_label1 = Label(master=content_box, background='red', text=night_wind, font=('黑体', 12))
    nightwind_label1.place(width=80, height=40, x=460, y=200)
    daypower_label1 = Label(master=content_box, background='red', text=day_power, font=('黑体', 12))
    daypower_label1.place(width=80, height=40, x=540, y=110)
    nightpower_label1 = Label(master=content_box, background='red', text=night_power, font=('黑体', 12))
    nightpower_label1.place(width=80, height=40, x=540, y=200)
    # 各项指标
    # 指标名
    target_label1 = (Label(master=content_box, text='感冒', background='red', font=('黑体', 12)))
    target_label1.place(width=155, height=50, x=210, y=280)
    target_label2 = Label(master=content_box, text='运动', background='red', font=('黑体', 12))
    target_label2.place(width=155, height=50, x=372, y=280)
    target_label3 = Label(master=content_box, text='洗车', background='red', font=('黑体', 12))
    target_label3.place(width=155, height=50, x=534, y=280)
    # 文字
    flu_brief = target['感冒']['brief']
    sport_brief = target['运动']['brief']
    car_washing_brief = target['洗车']['brief']
    flu_details = target['感冒']['details']
    sport_details = target['运动']['details']
    car_washing_details = target['洗车']['details']
    text1 = ttkbs.Text(master=content_box)
    text1.place(width=155, height=155, x=210, y=330)
    text1.insert(END, flu_brief)
    text1.insert(END, '\n')
    text1.insert(END, flu_details)
    text1.configure(state='disabled')
    text2 = ttkbs.Text(master=content_box)
    text2.place(width=155, height=155, x=372, y=330)
    text2.insert(END, sport_brief)
    text2.insert(END, '\n')
    text2.insert(END, sport_details)
    text2.configure(state='disabled')
    text3 = ttkbs.Text(master=content_box)
    text3.place(width=155, height=155, x=534, y=330)
    text3.insert(END, car_washing_brief)
    text3.insert(END, '\n')
    text3.insert(END, car_washing_details)
    text3.configure(state='disabled')
    # 更新内容窗口
    frame.update()
    # 日出日落
    sun_up = '日出\n' + data_sun['日出']
    sun_down = '日落\n' + data_sun['日落']
    up_box = ttkbs.Label(master=content_box, text=sun_up)
    up_box.place(width=50, height=40, x=302, y=25)
    down_box = ttkbs.Label(master=content_box, text=sun_down)
    down_box.place(width=50, height=40, x=432, y=25)



# 未来天气
def future_weather(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增新窗口
    content_box = ttkbs.LabelFrame(master=frame, text='未来天气')
    content_box.place(width=700, height=550, x=0, y=0)
    # 分割线
    ttkbs.Separator(master=content_box, orient=VERTICAL).place(width=1, height=360, x=233, y=100)
    ttkbs.Separator(master=content_box, orient=VERTICAL).place(width=1, height=360, x=467, y=100)
    # 天气信息
    forecast_wea = forecast_weath['casts']
    reporttime = '○ 更新时间 ' + str(forecast_weath['reporttime']).split()[1]
    refresh_label = ttkbs.Label(master=content_box, background='', text=reporttime)
    refresh_label.place(width=200, height=50, x=486, y=10)
    city_label = Label(master=content_box, text=city, font=('黑体', 16))
    city_label.place(width=234, height=50, x=234, y=10)
    # 图片
    global day_img1
    global night_img1
    day_img1 = PhotoImage(file='../resource/image/白天.png').subsample(2, 2)
    night_img1 = PhotoImage(file='../resource/image/夜晚.png')
    # 天气信息
    # 明天天气
    week_CN = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    forecast_wea1 = forecast_wea[1]
    d1 = str(forecast_wea1['date']).split('-')
    date1 = d1[1] + '/' + d1[2]
    dayweather1 = forecast_wea1['dayweather']
    daytemp1 = forecast_wea1['daytemp'] + '℃'
    daywind1 = forecast_wea1['daywind'] + '风'
    daypower1 = forecast_wea1['daypower'] + '级'
    nightweather1 = forecast_wea1['nightweather']
    nighttemp1 = forecast_wea1['nighttemp'] + '℃'
    nightwind1 = forecast_wea1['nightwind'] + '风'
    nightpower1 = forecast_wea1['nightpower'] + '级'
    date_label1 = Label(master=content_box, text=date1, font=('黑体', 12))
    date_label1.place(width=193, height=70, x=20, y=60)
    week_label1 = Label(master=content_box, text='明天', font=('黑体', 10))
    week_label1.place(width=193, height=40, x=20, y=110)
    day_img_label1 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=day_img1)
    day_img_label1.place(width=93, height=93, x=20, y=150)
    dayweather_label1 = Label(master=content_box, background='red', text=dayweather1, font=('黑体', 14))
    dayweather_label1.place(width=93, height=40, x=20, y=250)
    daytemp_label1 = Label(master=content_box, background='red', text=daytemp1, font=('黑体', 16))
    daytemp_label1.place(width=93, height=40, x=20, y=300)
    daywind_label1 = Label(master=content_box, background='red', text=daywind1, font=('黑体', 12))
    daywind_label1.place(width=93, height=40, x=20, y=350)
    daypower_label1 = Label(master=content_box, background='red', text=daypower1, font=('黑体', 12))
    daypower_label1.place(width=93, height=40, x=20, y=400)
    night_img_label1 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=night_img1)
    night_img_label1.place(width=93, height=93, x=123, y=150)
    nightweather_label1 = Label(master=content_box, background='red', text=nightweather1, font=('黑体', 14))
    nightweather_label1.place(width=93, height=40, x=123, y=250)
    nighttemp_label1 = Label(master=content_box, background='red', text=nighttemp1, font=('黑体', 16))
    nighttemp_label1.place(width=93, height=40, x=123, y=300)
    nightwind_label1 = Label(master=content_box, background='red', text=nightwind1, font=('黑体', 12))
    nightwind_label1.place(width=93, height=40, x=123, y=350)
    nightpower_label1 = Label(master=content_box, background='red', text=nightpower1, font=('黑体', 12))
    nightpower_label1.place(width=93, height=40, x=123, y=400)
    # 后天天气
    forecast_wea2 = forecast_wea[2]
    d2 = str(forecast_wea2['date']).split('-')
    date2 = d2[1] + '/' + d2[2]
    w2 = forecast_wea2['week']
    week2 = week_CN[int(w2) - 1]
    dayweather2 = forecast_wea2['dayweather']
    daytemp2 = forecast_wea2['daytemp'] + '℃'
    daywind2 = forecast_wea2['daywind'] + '风'
    daypower2 = forecast_wea2['daypower'] + '级'
    nightweather2 = forecast_wea2['nightweather']
    nighttemp2 = forecast_wea2['nighttemp'] + '℃'
    nightwind2 = forecast_wea2['nightwind'] + '风'
    nightpower2 = forecast_wea2['nightpower'] + '级'
    date_label2 = Label(master=content_box, text=date2, font=('黑体', 12))
    date_label2.place(width=194, height=70, x=253, y=60)
    week_label2 = Label(master=content_box, text=week2, font=('黑体', 10))
    week_label2.place(width=194, height=40, x=253, y=110)
    day_img_label2 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=day_img1)
    day_img_label2.place(width=93, height=93, x=253, y=150)
    dayweather_label2 = Label(master=content_box, background='red', text=dayweather2, font=('黑体', 14))
    dayweather_label2.place(width=93.5, height=40, x=253, y=250)
    daytemp_label2 = Label(master=content_box, background='red', text=daytemp2, font=('黑体', 16))
    daytemp_label2.place(width=93.5, height=40, x=253, y=300)
    daywind_label2 = Label(master=content_box, background='red', text=daywind2, font=('黑体', 12))
    daywind_label2.place(width=93.5, height=40, x=253, y=350)
    daypower_label2 = Label(master=content_box, background='red', text=daypower2, font=('黑体', 12))
    daypower_label2.place(width=93.5, height=40, x=253, y=400)
    night_img_label2 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=night_img1)
    night_img_label2.place(width=93, height=93, x=356.5, y=150)
    nightweather_label2 = Label(master=content_box, background='red', text=nightweather2, font=('黑体', 14))
    nightweather_label2.place(width=93.5, height=40, x=356.5, y=250)
    nighttemp_label2 = Label(master=content_box, background='red', text=nighttemp2, font=('黑体', 16))
    nighttemp_label2.place(width=93.5, height=40, x=356.5, y=300)
    nightwind_label2 = Label(master=content_box, background='red', text=nightwind2, font=('黑体', 12))
    nightwind_label2.place(width=93.5, height=40, x=356.5, y=350)
    nightpower_label2 = Label(master=content_box, background='red', text=nightpower2, font=('黑体', 12))
    nightpower_label2.place(width=93.5, height=40, x=356.5, y=400)
    # 2天后天气
    forecast_wea3 = forecast_wea[3]
    # print(forecast_wea3)
    d3 = str(forecast_wea3['date']).split('-')
    date3 = d3[1] + '/' + d3[2]
    w3 = forecast_wea3['week']
    week3 = week_CN[int(w3) - 1]
    dayweather3 = forecast_wea3['dayweather']
    daytemp3 = forecast_wea3['daytemp'] + '℃'
    daywind3 = forecast_wea3['daywind'] + '风'
    daypower3 = forecast_wea3['daypower'] + '级'
    nightweather3 = forecast_wea3['nightweather']
    nighttemp3 = forecast_wea3['nighttemp'] + '℃'
    nightwind3 = forecast_wea3['nightwind'] + '风'
    nightpower3 = forecast_wea3['nightpower'] + '级'
    date_label3 = Label(master=content_box, text=date3, font=('黑体', 12))
    date_label3.place(width=193, height=70, x=486, y=60)
    week_label3 = Label(master=content_box, text=week3, font=('黑体', 10))
    week_label3.place(width=193, height=40, x=486, y=110)
    day_img_label3 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=day_img1)
    day_img_label3.place(width=93, height=93, x=486, y=150)
    dayweather_label3 = Label(master=content_box, background='red', text=dayweather3, font=('黑体', 14))
    dayweather_label3.place(width=93, height=40, x=486, y=250)
    daytemp_label3 = Label(master=content_box, background='red', text=daytemp3, font=('黑体', 16))
    daytemp_label3.place(width=93, height=40, x=486, y=300)
    daywind_label3 = Label(master=content_box, background='red', text=daywind3, font=('黑体', 12))
    daywind_label3.place(width=93, height=40, x=486, y=350)
    daypower_label3 = Label(master=content_box, background='red', text=daypower3, font=('黑体', 12))
    daypower_label3.place(width=93, height=40, x=486, y=400)
    night_img_label3 = Label(master=content_box, background='lightblue', font=('黑体', 10), image=night_img1)
    night_img_label3.place(width=93, height=93, x=589, y=150)
    nightweather_label3 = Label(master=content_box, background='red', text=nightweather3, font=('黑体', 14))
    nightweather_label3.place(width=93, height=40, x=589, y=250)
    nighttemp_label3 = Label(master=content_box, background='red', text=nighttemp3, font=('黑体', 16))
    nighttemp_label3.place(width=93, height=40, x=589, y=300)
    nightwind_label3 = Label(master=content_box, background='red', text=nightwind3, font=('黑体', 12))
    nightwind_label3.place(width=93, height=40, x=589, y=350)
    nightpower_label3 = Label(master=content_box, background='red', text=nightpower3, font=('黑体', 12))
    nightpower_label3.place(width=93, height=40, x=589, y=400)


# 历史天气
def history_weather(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增新窗口
    content_box = ttkbs.LabelFrame(master=frame, text='历史天气')
    content_box.place(width=700, height=550, x=0, y=0)
    # 日期选择框
    date_box = ttkbs.DateEntry(master=content_box, dateformat=r'%Y-%m-%d')
    date_box.place(x=20, y=20)
    # 城市查询框
    city_label = Label(master=content_box, text='历史', font=('黑体', 14))
    city_label.place(width=100, height=40, x=300, y=20)
    city_select_box = ttkbs.Entry(master=content_box)
    city_select_box.place(width=160, x=450, y=20)
    city_select_box.insert(END, '请输入城市名')

    # 清空输入框事件
    def clean(event):
        city_select_box.delete(0, END)

    # 绑定鼠标左键
    city_select_box.bind('<Button-1>', clean)
    # 搜索按钮
    search_box = ttkbs.Button(master=content_box, text='搜索',
                              command=lambda: [Component.search_thread(date_box=date_box, city_box=city_select_box,
                                                                       text_box=weather_data_box)])
    search_box.place(width=60, x=620, y=20)
    # 天气内容 表格
    weather_data_box = ttkbs.Treeview(master=content_box,
                                      columns=['城市', '日期', '天气状况', '最低/最高气温', '风力风向'], show=HEADINGS)
    weather_data_box.place(width=660, height=430, x=20, y=80)
    # 列名
    weather_data_box.heading(0, text='城市')
    weather_data_box.heading(1, text='日期')
    weather_data_box.heading(2, text='天气状况')
    weather_data_box.heading(3, text='最低/最高气温')
    weather_data_box.heading(4, text='风力风向')
    weather_data_box.column(0, width=10, anchor=CENTER)
    weather_data_box.column(1, width=80, anchor=CENTER)
    weather_data_box.column(2, width=40, anchor=CENTER)
    weather_data_box.column(3, width=60, anchor=CENTER)
    weather_data_box.column(4, width=130, anchor=CENTER)
    # 增加滚动条
    table_bar = ttkbs.Scrollbar(master=content_box, orient=VERTICAL, command=weather_data_box.yview, bootstyle=ROUND)
    weather_data_box.configure(yscrollcommand=table_bar.set)
    table_bar.place(height=430, x=680, y=80)
    # 写入
    for row in data_history:
        weather_data_box.insert('', END, values=row)
    # history_thread(city_CN=city0, date=year_month, box=weather_data_box)  # 获取数据


# 数据图表
def data_view(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增选项卡
    tab_box = ttkbs.Notebook(master=frame)
    tab_box.place(width=700, height=550, x=0, y=0)  # , x=260, y=110
    tab1 = ttkbs.Canvas(master=tab_box, width=700, height=500)
    tab2 = ttkbs.Canvas(master=tab_box, width=700, height=500)
    tab3 = ttkbs.Canvas(master=tab_box, width=700, height=500)
    tab4 = ttkbs.Canvas(master=tab_box, width=700, height=500)
    tab5 = ttkbs.Frame(master=tab_box, width=700, height=500)
    # 表格
    columns = ['排名', '城市', '所在省', '今天', '平均']
    # 最高气温排行榜
    hot_title_label = ttkbs.Label(master=tab5, font=('黑体', 14))
    hot_title_label.place(width=300, height=40, x=40, y=10)
    hot_update_label = ttkbs.Label(master=tab5)
    hot_update_label.place(width=300, height=20, x=40, y=50)
    hot_table = ttkbs.Treeview(master=tab5, columns=columns, show=HEADINGS)
    hot_table.place(width=320, height=420, x=10, y=80)
    i = 0
    for item1 in columns:
        hot_table.heading(i, text=item1)
        i += 1
    hot_table.column(0, width=30, anchor=CENTER)
    hot_table.column(1, width=50, anchor=CENTER)
    hot_table.column(2, width=50, anchor=CENTER)
    hot_table.column(3, width=50, anchor=CENTER)
    hot_table.column(4, width=30, anchor=CENTER)
    # 增加滚动条
    hot_bar = ttkbs.Scrollbar(master=tab5, orient=VERTICAL, command=hot_table.yview, bootstyle=ROUND)
    hot_table.configure(yscrollcommand=hot_bar.set)
    hot_bar.place(height=420, x=330, y=80)

    # 最低气温排行榜
    cold_title_label = ttkbs.Label(master=tab5, font=('黑体', 14))
    cold_title_label.place(width=300, height=40, x=380, y=10)
    cold_update_label = ttkbs.Label(master=tab5)
    cold_update_label.place(width=300, height=20, x=380, y=50)
    cold_table = ttkbs.Treeview(master=tab5, columns=columns, show=HEADINGS)
    cold_table.place(width=320, height=420, x=354, y=80)
    j = 0
    for item2 in columns:
        cold_table.heading(j, text=item2)
        j += 1
    cold_table.column(0, width=30, anchor=CENTER)
    cold_table.column(1, width=50, anchor=CENTER)
    cold_table.column(2, width=50, anchor=CENTER)
    cold_table.column(3, width=50, anchor=CENTER)
    cold_table.column(4, width=30, anchor=CENTER)
    # 增加滚动条
    cold_bar = ttkbs.Scrollbar(master=tab5, orient=VERTICAL, command=cold_table.yview, bootstyle=ROUND)
    cold_table.configure(yscrollcommand=cold_bar.set)
    cold_bar.place(height=420, x=674, y=80)
    # 增加标签
    tab_box.add(text='上月天气状况', child=tab1)
    tab_box.add(text='本市前30天风向频率', child=tab2)
    tab_box.add(text='本市前30天气温', child=tab3)
    tab_box.add(text='昨天部分城市最高温度', child=tab4)
    tab_box.add(text='极端温度实时排行榜', child=tab5)
    # 关闭所有图表
    Chart.plt_close()
    # 嵌入图表
    Chart.chart_pie(box=tab1, city=city0)
    Chart.chart_polar(box=tab2, city=city0)
    Chart.chart_line(box=tab3, city=city0)
    Chart.chart_bar(box=tab4)
    Chart.hot_cold_thread(hot_title_label=hot_title_label, hot_update_label=hot_update_label, hot_box=hot_table,
                          cold_title_label=cold_title_label, cold_update_label=cold_update_label, cold_box=cold_table)


# 实况图片
def live_picture(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增选项卡
    tab_box = ttkbs.Notebook(master=frame)
    tab_box.place(width=700, height=550, x=0, y=0)  # , borderwidth=1, relief='groove'
    tab1 = ttkbs.Frame(master=tab_box)
    tab2 = ttkbs.Frame(master=tab_box)
    tab3 = ttkbs.Frame(master=tab_box)
    tab4 = ttkbs.Frame(master=tab_box)
    tab5 = ttkbs.Frame(master=tab_box)
    # 增加标签
    tab_box.add(text='1小时累计降水实况', child=tab1)
    tab_box.add(text='3小时累计降水实况', child=tab2)
    tab_box.add(text='小时最低能见度实况', child=tab3)
    tab_box.add(text='小时气温实况', child=tab4)
    tab_box.add(text='卫星云量实况', child=tab5)
    # 嵌入图片
    Photo_show.ImageApp1(tab1)
    Photo_show.ImageApp2(tab2)
    Photo_show.ImageApp3(tab3)
    Photo_show.ImageApp4(tab4)
    Photo_show.ImageApp5(tab5)
    # 刷新按钮  padding[左,上,右,下]
    ttkbs.Button(master=tab1, text='刷\n新', padding=[10, 15, 10, 15],
                 command=lambda: [Download_photo.download_one(1), Photo_show.ImageApp1(tab1)]).place(x=640, y=20)
    ttkbs.Button(master=tab2, text='刷\n新', padding=[10, 15, 10, 15],
                 command=lambda: [Download_photo.download_one(2), Photo_show.ImageApp2(tab2)]).place(x=640, y=20)
    ttkbs.Button(master=tab3, text='刷\n新', padding=[10, 15, 10, 15],
                 command=lambda: [Download_photo.download_one(3), Photo_show.ImageApp3(tab3)]).place(x=640, y=20)
    ttkbs.Button(master=tab4, text='刷\n新', padding=[10, 15, 10, 15],
                 command=lambda: [Download_photo.download_one(4), Photo_show.ImageApp4(tab4)]).place(x=640, y=20)
    ttkbs.Button(master=tab5, text='刷新',
                 command=lambda: [Download_photo.download_one(5), Photo_show.ImageApp5(tab5)]).place(x=480, y=6)
    # 原图按钮
    ttkbs.Button(master=tab1, text='原\n图', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.open_original(1)).place(x=640, y=100)
    ttkbs.Button(master=tab2, text='原\n图', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.open_original(2)).place(x=640, y=100)
    ttkbs.Button(master=tab3, text='原\n图', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.open_original(3)).place(x=640, y=100)
    ttkbs.Button(master=tab4, text='原\n图', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.open_original(4)).place(x=640, y=100)
    ttkbs.Button(master=tab5, text='原图', command=lambda: Photo_show.open_original(5)).place(x=550, y=6)
    # 另存为
    ttkbs.Button(master=tab1, text='另\n存', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.fileSave(1)).place(x=640, y=180)
    ttkbs.Button(master=tab2, text='另\n存', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.fileSave(2)).place(x=640, y=180)
    ttkbs.Button(master=tab3, text='另\n存', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.fileSave(3)).place(x=640, y=180)
    ttkbs.Button(master=tab4, text='另\n存', padding=[10, 15, 10, 15],
                 command=lambda: Photo_show.fileSave(4)).place(x=640, y=180)
    ttkbs.Button(master=tab5, text='另存', command=lambda: Photo_show.fileSave(5)).place(x=620, y=6)


# 设置
def setting(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增新窗口
    content_box = ttkbs.LabelFrame(master=frame, text='设置')
    content_box.place(width=700, height=550, x=0, y=0)
    ttkbs.Label(master=frame, text='设置', font=('黑体', 20)).place(x=40, y=30)
    ttkbs.Separator(master=frame, orient='horizontal').place(width=150, height=2, x=40, y=70)
    # 定义变量
    var_auto = ttkbs.IntVar()
    var_notice = ttkbs.IntVar()
    var_dark = ttkbs.IntVar()
    autorun = ttkbs.Checkbutton(master=frame, text='开机自启', variable=var_auto, offvalue=0, onvalue=1, bootstyle='round-toggle',
                                command=lambda: Component.auto_boot(var_auto))
    autorun.place(x=40, y=100)

    notice_btn = ttkbs.Checkbutton(master=frame, text='服务通知', bootstyle='round-toggle', variable=var_notice, offvalue=0, onvalue=1,
                                   command=lambda: Component.service_notice(var_notice))
    notice_btn.place(x=40, y=150)

    dark_btn = ttkbs.Checkbutton(master=frame, text='夜间模式', variable=var_dark, offvalue=0, onvalue=1,
                                 bootstyle='round-toggle', command=lambda: Component.theme_change(var_dark))
    dark_btn.place(x=40, y=200)
    data = pd.read_csv('../resource/file/setting.csv')
    dark = data['dark'].values[0]
    auto_boot = data['auto_boot'].values[0]
    notice = data['notice'].values[0]
    if dark == 1:
        dark_btn.invoke()
    else:
        pass
    if auto_boot == 1:
        autorun.invoke()
    else:
        pass
    if notice == 1:
        notice_btn.invoke()
    else:
        pass

    ttkbs.Label(master=frame, text='当前版本： Alpha 2023.05.07').place(width=250, height=30, x=40, y=250)
    ttkbs.Label(master=frame, text='功能介绍：\n新增夜间模式。\n解决了页面卡顿的问题。\n修复了已知问题。').place(
        width=200, height=100, x=40, y=300)
    ttkbs.Button(master=frame, text='检查更新', bootstyle='info-link').place(width=100, height=30, x=40, y=430)


# 关于我们
def about_we(frame):
    # 清空内容窗口
    Component.box_clear(frame=frame)
    # 新增新窗口
    content_box = ttkbs.LabelFrame(master=frame, text='关于我们')
    content_box.place(width=700, height=550, x=0, y=0)
    # 内容
    about_labele = ttkbs.Label(master=content_box, text='关于我们', font=('楷体', 20, 'bold'))
    about_labele.place(width=200, height=50, x=160, y=20)
    # 分割线
    line = ttkbs.Separator(master=content_box)
    line.place(width=340, height=2, x=160, y=70)
    # 广告语
    aim_label = ttkbs.Label(master=content_box, text='其实，\n  我们只是数据的搬运工！', font=('楷体', 14, 'bold'))
    aim_label.place(width=300, height=50, x=160, y=100)
    # 愿景
    vision_label = ttkbs.Label(master=content_box, text='愿景：\n推进现代数字天气的发展', font=('楷体', 14))
    vision_label.place(width=300, height=50, x=160, y=160)
    # 项目成员
    # member_label = ttkbs.Label(master=content_box, text='小组成员：\n 李伶  陈梓琳\n薛才钰 陈璇靖', font=('黑体', 14))
    member_label = ttkbs.Label(master=content_box, text='创作者：\n 李伶  陈梓琳\n薛才钰 陈璇靖', font=('楷体', 14))
    member_label.place(width=440, height=100, x=160, y=210)
    # 数据来源
    data_label = ttkbs.Label(master=content_box,
                             text='所有数据均来自于：\n腾讯位置服务 高德地图 心知天气\n天气后报 天气史 2345天气王\n中国气象数据中心',
                             font=('楷体', 14))
    data_label.place(width=440, height=120, x=160, y=300)
    # 联系方式
    relation_label = ttkbs.Label(master=content_box, text='如有侵权，请联系：\n邮箱：yy378827@gmail.com\n电话：16700000000',
                                 font=('华文行楷', 12))
    relation_label.place(width=440, height=80, x=160, y=420)
