import ttkbootstrap as ttkbs
from tkinter.filedialog import asksaveasfilename
from ttkbootstrap import PhotoImage
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

import Download_photo

# 启动前全部下载
Download_photo.download_all()


# 嵌入图片
# 全国1小时累计降水量实况
class ImageApp1(ttkbs.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0)
        self.create_widgets()

    def create_widgets(self):
        try:
            # 读取图片
            self.image = Image.open("../resource/live_picture/全国1小时累计降水量实况.png")
            # 缩小图片
            self.image = self.image.resize((int(self.image.width * 0.292), int(self.image.height * 0.292)))
            # 将图片转换为Tkinter格式
            self.tk_image = ImageTk.PhotoImage(self.image)
            # 显示图片
            self.label = ttkbs.Label(self, image=self.tk_image)
            self.label.pack()
        except:
            print('图片读取失败')
        # print('显示')


# 全国3小时累计降水量实况
class ImageApp2(ttkbs.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0)
        self.create_widgets()

    def create_widgets(self):
        try:
            # 读取图片
            self.image = Image.open("../resource/live_picture/全国3小时累计降水量实况.png")
            # 缩小图片
            self.image = self.image.resize((int(self.image.width * 0.292), int(self.image.height * 0.292)))
            # 将图片转换为Tkinter格式
            self.tk_image = ImageTk.PhotoImage(self.image)
            # 显示图片
            self.label = ttkbs.Label(self, image=self.tk_image)
            self.label.pack()
            # print('显示')
        except:
            print('图片读取失败')



# 全国小时最低能见度实况
class ImageApp3(ttkbs.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0)
        self.create_widgets()

    def create_widgets(self):
        try:
            # 读取图片
            self.image = Image.open("../resource/live_picture/全国小时最低能见度实况.png")
            # 获取图片宽度和高度
            self.width, self.height = self.image.size
            # 切割图片
            self.image = self.image.crop((0, 0, self.width - int(self.width * 0.04), self.height))
            # 缩小图片
            self.image = self.image.resize((int(self.image.width * 0.35), int(self.image.height * 0.35)))
            # 将图片转换为Tkinter格式
            self.tk_image = ImageTk.PhotoImage(self.image)
            # 显示图片
            self.label = ttkbs.Label(self, image=self.tk_image)
            self.label.pack()
            # print('显示')
        except:
            print('图片读取失败')



# 全国小时气温实况
class ImageApp4(ttkbs.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0)
        self.create_widgets()

    def create_widgets(self):
        try:
            # 读取图片
            self.image = Image.open("../resource/live_picture/全国小时气温实况.png")
            # 缩小图片
            self.image = self.image.resize((int(self.image.width * 0.346), int(self.image.height * 0.346)))
            # 将图片转换为Tkinter格式
            self.tk_image = ImageTk.PhotoImage(self.image)
            # 显示图片
            self.label = ttkbs.Label(self, image=self.tk_image)
            self.label.pack()
            # print('显示')
        except:
            print('图片读取失败')


# 卫星云量图
class ImageApp5(ttkbs.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=4, y=40)
        self.create_widgets()

    def create_widgets(self):
        try:
            # 读取图片
            self.image = Image.open("../resource/live_picture/卫星云量图.png")
            # 缩小图片
            self.image = self.image.resize((int(self.image.width * 0.95), int(self.image.height * 0.95)))
            # 将图片转换为Tkinter格式
            self.tk_image = ImageTk.PhotoImage(self.image)
            # 显示图片
            self.label = ttkbs.Label(self, image=self.tk_image)
            self.label.pack()
            # print('显示')
        except:
            print('图片读取失败')


# 打开新窗口 原图功能
def open_original(flag):
    # 创建窗口
    image_win = ttkbs.Toplevel(title='原图')
    image_win.geometry('1000x700')
    # image_win.position_center()
    image_win.iconphoto(False, PhotoImage(file='../resource/image/picture_icon.png'))
    # 创建框架
    frame = ttkbs.Frame(master=image_win, borderwidth=2, relief='groove')
    frame.place(relwidth=0.975, relheight=0.96, relx=0.01, rely=0.015)
    # 创建画布
    canvas = ttkbs.Canvas(master=frame)
    canvas.place(relwidth=1, relheight=1, relx=0, rely=0)
    # 加载图片
    try:
        global image
        if flag == 1:
            image = Image.open('../resource/live_picture/全国1小时累计降水量实况.png')
        elif flag == 2:
            image = Image.open('../resource/live_picture/全国3小时累计降水量实况.png')
        elif flag == 3:
            image = Image.open('../resource/live_picture/全国小时最低能见度实况.png')
        elif flag == 4:
            image = Image.open('../resource/live_picture/全国小时气温实况.png')
        elif flag == 5:
            image = Image.open('../resource/live_picture/卫星云量图.png')
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=photo, anchor="nw")
        # 滚动条
        yscrollbar = ttkbs.Scrollbar(master=image_win, orient=VERTICAL, command=canvas.yview)
        xscrollbar = ttkbs.Scrollbar(master=image_win, orient=HORIZONTAL, command=canvas.xview)  # , bootstyle=ROUND
        canvas.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
        canvas.place(x=0, y=0)
        yscrollbar.pack(side=RIGHT, fill=Y)
        xscrollbar.pack(side=BOTTOM, fill=X)
        # 设置滚动区域
        canvas.config(scrollregion=canvas.bbox("all"))
    except:
        print('图片读取失败')
    # 显示窗口
    image_win.mainloop()


# 图片另存功能
def fileSave(flag):
    global image_f, file_path
    try:
        if flag == 1:
            image_f = Image.open('../resource/live_picture/全国1小时累计降水量实况.png')
            file_path = asksaveasfilename(initialfile='全国1小时累计降水量实况',
                                          defaultextension='.png')  # 设置保存文件，设置文件名，指定文件名后缀为.png
        elif flag == 2:
            image_f = Image.open('../resource/live_picture/全国3小时累计降水量实况.png')
            file_path = asksaveasfilename(initialfile='全国3小时累计降水量实况',
                                          defaultextension='.png')
        elif flag == 3:
            image_f = Image.open('../resource/live_picture/全国小时最低能见度实况.png')
            file_path = asksaveasfilename(initialfile='全国小时最低能见度实况',
                                          defaultextension='.png')
        elif flag == 4:
            image_f = Image.open('../resource/live_picture/全国小时气温实况.png')
            file_path = asksaveasfilename(initialfile='全国小时气温实况',
                                          defaultextension='.png')
        elif flag == 5:
            image_f = Image.open('../resource/live_picture/卫星云量图.png')
            file_path = asksaveasfilename(initialfile='卫星云量图',
                                          defaultextension='.png')

        image_f.save(file_path)
    except:
        print('保存失败')

# 多线程更新图
# def update_thread(flag):
#     update_t = threading.Thread(target=Download_photo.download_one, args=(flag,))
#     update_t.start()
#     # 阻塞线程等待该线程完成再继续执行下一步
#     update_t.join()
