import threading
import ttkbootstrap as ttkbs
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fct
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from pylab import mpl

import Chart_data

mpl.rcParams['font.sans-serif'] = ['SimHei']    # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
np.seterr(divide='ignore', invalid='ignore')    # RuntimeWarning: invalid value encountered in true_divide
plt.style.use('ggplot') # 设置风格

# 清除所有图表
def plt_close():
    plt.close("all")


# 上月天气状况
def chart_pie(box, city):
    try:
        # 数据
        labels1 = ['晴天', '雨/雪', '多云/阴天', '其他']
        labels2 = ['白天', '夜晚', '白天', '夜晚', '白天', '夜晚', '白天', '夜晚']
        colors1 = ['#e50000', '#0165fc', '#9400D3', '#708090']
        colors2 = ['#ff000d', '#fd4659', '#3e82fc', '#1E90FF', '#be03fd', '#d94ff5', '#889191', '#9ba1a1']
        x1 = Chart_data.data_pie()['x1']
        x2 = Chart_data.data_pie()['x2']
        # 设置图幅大小
        fig = plt.figure(figsize=(7, 5), dpi=100)
        # 设置图幅位置
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.81])
        # 设置标题
        ax.set_title(city + '上月天气状况')
        # 绘制图表
        ax.pie(labels=labels1, x=x1, colors=colors1, autopct='%1.1f%%', radius=0.65, wedgeprops={'width': 0.35, 'edgecolor': 'w'},
               textprops={'color': '#191970'})  # 内圆
        ax.pie(labels=labels2, x=x2, colors=colors2, wedgeprops={'width': 0.35, 'edgecolor': 'w'})  # 外圆
        ax.text(x=0, y=0, s=city, ha='center', va='center', fontsize=16)
        # 文本框
        day_text = f'白天状况\n晴天:{x2[0]}天\n雨/雪:{x2[2]}天\n多云/阴天:{x2[4]}天\n其他:{x2[6]}天'
        night_text = f'夜晚状况\n晴天:{x2[1]}天\n雨/雪:{x2[3]}天\n多云/阴天:{x2[5]}天\n其他:{x2[7]}天'
        ax.text(x=-2, y=-0.80, s=day_text, fontsize=10,
                bbox=dict(boxstyle="round", facecolor='#d3dada', edgecolor='b', alpha=0.3))
        ax.text(x=-2, y=-1.45, s=night_text, fontsize=10,
                bbox=dict(boxstyle="round", facecolor='#383f8f', edgecolor='b', alpha=0.3))
        # 设置图例
        ax.legend(['晴天', '雨/雪', '多云/阴天', '其他'], loc=(0.96, -0.09))
        # 背景透明
        # fig.patch.set_alpha(0)
        # 嵌入界面
        canvas = fct(fig, master=box)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except:
        ttkbs.Label(master=box, text='无数据').pack(anchor='center', pady=200)


# 本市前30天风向频率
def chart_polar(box, city):
    try:
        data = Chart_data.data_polar()
        categories = list(data.keys())
        values = list(data.values())
        N = len(categories)
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]
        values += values[:1]
        # 设置图幅的大小
        fig = plt.figure(figsize=(7, 5), dpi=100)
        # 设置图幅位置
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.75], polar=True, projection='polar')
        ax.set_theta_offset(np.pi / 2)
        # 设置背景
        ax.set_facecolor('w')
        # 轴线
        ax.grid(ls="--", lw=0.5, color="#4E616C")
        ticks = np.linspace(0, 2 * np.pi, len(angles) - 1, endpoint=False)
        ax.set_thetagrids(ticks * 180 / np.pi, labels=categories)
        ax.set_rlabel_position(-70)
        ax.set_title(city + '前30天风向频率')
        max_value = max(data.values())
        step = max_value // 3
        plt.yticks(range(0, max_value + 1, step), [str(i) for i in range(0, max_value + 1, step)])
        ax.plot(angles, values, linewidth=1, linestyle='solid', color='#0a5f38')
        ax.fill(angles, values, '#04f489', alpha=0.1)
        # 嵌入界面
        canvas = fct(fig, master=box)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except:
        ttkbs.Label(master=box, text='无数据').pack(anchor='center', pady=200)


# 本市前30天气温
def chart_line(box, city):
    # 数据
    x = Chart_data.data_line()['日期']
    hot = Chart_data.data_line()['最高温度']
    cold = Chart_data.data_line()['最低温度']
    # 设置图幅大小
    fig = plt.figure(figsize=(7, 5), dpi=100)
    # 设置图幅位置
    ax = fig.add_axes([0.1, 0.12, 0.8, 0.79])
    # 设置背景
    ax.set_facecolor('w')
    # 轴线
    ax.grid(ls="--", lw=0.5, color="#4E616C")
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    # 设置标题
    ax.set_title(city + '前30天气温')
    # 设置轴标签名
    plt.xlabel(xlabel='时 间')
    plt.ylabel(ylabel='温 度')
    # x轴标签名旋转
    # ax.set_xticklabels(labels = x, rotation=-60)
    # 绘制图表
    ax.plot(x, hot, marker='o', color='red', markersize=5, markerfacecolor='white')
    ax.plot(x, cold, marker='o', color='blue', markersize=5, markerfacecolor='white')
    # 设置填充颜色
    ax.fill_between(x, hot, cold, facecolor='lightblue', alpha=0.5)
    # 统计最值
    try:
        # 统计温度最值
        hot_text = f'最高:{max(hot)}℃'
        cold_text = f'最低:{min(cold)}℃'
        # 获取轴最值
        y_max = max(plt.yticks()[0])
        y_min = min(plt.yticks()[0])
        x_min = -5
    except:
        # 无数据
        hot_text = '最高: 无数据'
        cold_text = '最低: 无数据'
        # 定义轴最值
        y_max = 0.05
        y_min = -0.05
        x_min = 0
    ax.text(x=x_min, y=y_max, s=hot_text, fontsize=10,
            bbox=dict(boxstyle="round", facecolor='red', edgecolor='springgreen', alpha=0.5))
    ax.text(x=x_min, y=y_min, s=cold_text, fontsize=10,
            bbox=dict(boxstyle="round", facecolor='blue', edgecolor='springgreen', alpha=0.5))
    # 设置图例
    ax.legend(["最高", "最低"], loc=(0.94, 0.96))
    # 背景透明
    # fig.patch.set_alpha(0)
    # 嵌入界面
    canvas = fct(fig, master=box)
    canvas.draw()
    canvas.get_tk_widget().pack()


# 昨天部分城市温度
def chart_bar(box):
    # 数据
    x = Chart_data.data_bar()['城市']
    height = Chart_data.data_bar()['数据']
    # 设置图幅大小
    fig = plt.figure(figsize=(7, 5), dpi=100)
    # 设置图幅位置
    ax = fig.add_axes([0.09, 0.16, 0.97, 0.75])
    # 设置背景
    ax.set_facecolor('w')
    # 轴线
    ax.grid(ls="--", lw=0.5, color="#4E616C")
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    # 设置标题
    ax.set_title('昨天部分城市最高温度')
    # 设置轴标签名
    plt.ylabel(ylabel='温 度')
    # 设置最左边的轴线为黑色
    ax.spines['bottom'].set_color('black')
    # x轴标签名旋转
    # ax.set_xticklabels(labels=x, rotation=-90)
    # 创建归一化对象
    norm = Normalize(vmin=min(height), vmax=max(height))
    # 创建颜色映射对象
    cmap = plt.get_cmap('YlOrRd')
    sm = ScalarMappable(norm=norm, cmap=cmap)
    # 绘制图表，并为每个条形添加颜色
    for i in range(len(x)):
        ax.bar(x=x[i], height=height[i], color=sm.to_rgba(height[i]))
    # 添加颜色条
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_ticks([np.min(height), np.max(height)])
    # 背景透明
    # fig.patch.set_alpha(0)
    # 嵌入界面
    canvas = fct(fig, master=box)
    canvas.draw()
    canvas.get_tk_widget().pack()


# 极端天气排行榜
def hot_cold_thread(hot_title_label, hot_update_label, hot_box, cold_title_label, cold_update_label, cold_box):
    # 开启线程
    ranking_thread = threading.Thread(target=Chart_data.data_table, args=(
        hot_title_label, hot_update_label, hot_box, cold_title_label, cold_update_label, cold_box))
    ranking_thread.start()

# def charts_over(box1, box2, box3, city):
#     # 开启线程
#     t1 = threading.Thread(target=chart_pie, args=(box1, city))
#     t2 = threading.Thread(target=chart_line, args=(box2, city))
#     t3 = threading.Thread(target=chart_polar, args=(box3, city))
#     # t4 = threading.Thread(target=chart_bar, args=box4)
#     # 开始运行
#     t1.start()
#     t2.start()
#     t3.start()


# 上月降水量统计
# def chart_bar(box):
#     # 数据
#     x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
#          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
#     height = [289, 293, 381, 128, 376, 298, 239, 276, 278, 287, 289, 293, 381, 128, 376, 298, 239, 276, 278, 287, 289,
#               293, 381, 128, 376, 298, 239, 276, 278, 287]
#     # 设置风格
#     plt.style.use('ggplot')
#     # 设置图幅大小
#     fig = plt.figure(figsize=(7, 5), dpi=100)
#     # 设置图幅位置
#     ax = fig.add_axes([0.1, 0.12, 0.8, 0.79])
#     # 设置标题
#     ax.set_title('上月降水量统计')
#     # 设置轴标签名
#     plt.xlabel(xlabel='日 期')
#     # 绘制图表
#     ax.bar(x=x, height=height, width=0.8)
#     # 设置图例
#     # ax.legend(loc=(-0.3, 0.75))
#     # 嵌入界面
#     canvas = fct(fig, master=box)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
