import pandas as pd
import ttkbootstrap as ttkbs


# 工具方法
# 清空容器
def clean(box):
    for widget in box.winfo_children():
        widget.destroy()


# 夜间模式
def theme_change(var):
    # 获取offvalue和onvalue
    val = var.get()
    # print(val)
    style = ttkbs.Style()
    file = '../resource/file/setting.csv'
    dt = pd.read_csv(file)
    if val == 0:    # 关闭
        style.theme_use('litera')   # 日间模式
        dt['dark'] = [0]
        dt.to_csv(file, index=False)
    if val == 1:    # 打开
        style.theme_use('solar')   # 夜间模式
        dt['dark'] = [1]
        dt.to_csv(file, index=False)


# 默认夜间或日间
def dark_default():
    file = '../resource/file/setting.csv'
    dt = pd.read_csv(file)
    val = dt['dark'].values[0]
    # print(val)
    style = ttkbs.Style()
    if val == 0:  # 关闭
        style.theme_use('litera')  # 日间模式
    if val == 1:  # 打开
        style.theme_use('solar')  # 夜间模式 darkly