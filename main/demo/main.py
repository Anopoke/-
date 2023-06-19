import time
import threading
from tkinter import *
import ttkbootstrap as ttkbs
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
from Component import now_time, dark_default


# 根窗口配置
def application(root):
    start = time.time()
    # print(start)
    root.geometry('1000x700')
    root.position_center()
    root.resizable(False, False)  # 不可调整大小, borderwidth=10, relief='groove'
    root.iconphoto(False, PhotoImage(file='../resource/image/root_icon.png'))
    # 样式风格
    style = ttkbs.Style()
    style.configure('TButton', font=('黑体', 10))
    # 画线
    ttkbs.Separator(master=root).place(width=940, height=2, x=30, y=90)
    # 更新根窗体
    root.update()
    # 引入内容
    import Content
    # logo
    logo = ttkbs.PhotoImage(file='../resource/image/logo.png').subsample(2, 2)
    logo_box = ttkbs.Button(master=root, image=logo, bootstyle='danger-link', command=lambda: Content.today_weather(frame=frame))
    logo_box.place(width=250, height=90, x=100, y=0)
    # 关闭预启动界面
    preload_window.destroy()
    # 显示时间
    now_time()
    # 导航栏
    navigation_bar = ttkbs.LabelFrame(text='Tool')
    navigation_bar.place(width=200, height=550, x=40, y=110)
    # 内容框
    frame = ttkbs.Frame(master=root)
    frame.place(width=700, height=550, x=260, y=110)
    # 分割线
    ttkbs.Separator(master=navigation_bar).place(width=160, height=2, x=20, y=187)
    ttkbs.Separator(master=navigation_bar).place(width=160, height=2, x=20, y=313)

    # 今日天气
    img1 = ttkbs.PhotoImage(file='../resource/image/今.png')
    today_button = ttkbs.Button(master=navigation_bar, text='日天气', bootstyle=(PRIMARY, "outline-button"), image=img1,
                                compound=LEFT, command=lambda: Content.today_weather(frame=frame))
    today_button.place(relx=0.04, rely=0.02, relwidth=0.92, relheight=0.1)
    # 未来天气
    img2 = ttkbs.PhotoImage(file='../resource/image/未.png')
    future_button = ttkbs.Button(master=navigation_bar, text='来天气', bootstyle=(WARNING, "outline-button"),
                                 image=img2, compound=LEFT, command=lambda: Content.future_weather(frame=frame))
    future_button.place(relx=0.04, rely=0.13, relwidth=0.92, relheight=0.1)
    # 历史天气
    img3 = ttkbs.PhotoImage(file='../resource/image/历史.png')
    history_button = ttkbs.Button(master=navigation_bar, text='历史天气', bootstyle=(SUCCESS, "outline-button"),
                                  image=img3, compound=LEFT, command=lambda: Content.history_weather(frame=frame))
    history_button.place(relx=0.04, rely=0.24, relwidth=0.92, relheight=0.1)
    # 数据图表
    img4 = ttkbs.PhotoImage(file='../resource/image/图表.png')
    data_view_button = ttkbs.Button(master=navigation_bar, text='数据图表', bootstyle=(DANGER, "outline-button"),
                                    image=img4, compound=LEFT, command=lambda: Content.data_view(frame=frame))
    data_view_button.place(relx=0.04, rely=0.37, relwidth=0.92, relheight=0.1)
    # 全国实况
    img5 = ttkbs.PhotoImage(file='../resource/image/预测.png')
    satellite_button = ttkbs.Button(master=navigation_bar, text='全国实况', bootstyle=(INFO, "outline-button"),
                                    image=img5, compound=LEFT, command=lambda: Content.live_picture(frame=frame))
    satellite_button.place(relx=0.04, rely=0.48, relwidth=0.92, relheight=0.1)
    # 设置
    img6 = ttkbs.PhotoImage(file='../resource/image/设置.png')
    setting_button = ttkbs.Button(master=navigation_bar, text='设置', bootstyle=(DARK, "outline-button"),
                                    image=img6, compound=LEFT, command=lambda: Content.setting(frame=frame))
    setting_button.place(relx=0.04, rely=0.61, relwidth=0.92, relheight=0.1)
    # 关于我们
    img7 = ttkbs.PhotoImage(file='../resource/image/关于我们.png')
    about_button = ttkbs.Button(master=navigation_bar, text='关于我们', bootstyle=(DARK, "outline-button"), image=img7,
                                compound='left', command=lambda: Content.about_we(frame=frame))
    about_button.place(relx=0.04, rely=0.72, relwidth=0.92, relheight=0.1)
    # 进入应用程序 显示今日天气
    Content.today_weather(frame=frame)
    # 保留上次夜间模式
    dark_default()
    # 还原根窗口
    root.deiconify()
    end = time.time()
    # print(end)
    print(f'启动耗时：{end - start}秒')
    # 根窗口持久化
    root.mainloop()


# 主程序
if __name__ == '__main__':
    # 根窗口
    root = ttkbs.Window(title='', themename='cosmo')  # cerculean
    # 隐藏根窗口，直到它完全加载
    root.withdraw()
    # 预加载界面
    preload_window = ttkbs.Toplevel(overrideredirect=True)
    preload_window.geometry('+630+300')
    image = Image.open('../resource/image/welcome.png')
    photo = ImageTk.PhotoImage(image)
    ttkbs.Label(preload_window, image=photo).pack()
    # 根窗口配置-主线程-守护线程
    main_thread = threading.Thread(target=application(root), daemon=True)
    main_thread.start()
