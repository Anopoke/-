import requests
import re

# 图片来源：国家气象数据中心
url = 'https://data.cma.cn'


# 下载全部图片
def download_all():
    response = requests.get(url)
    # 编码一致
    response.encoding = response.apparent_encoding
    # 定义匹配链接和文件路径
    image_info = [
        ('http://image.data.cma.cn/vis/1kmCLDAS_ChnPre01/.*?', '../resource/live_picture/全国1小时累计降水量实况'),
        ('http://image.data.cma.cn/vis/1kmCLDAS_ChnPre03/.*?', '../resource/live_picture/全国3小时累计降水量实况'),
        ('http://image.data.cma.cn/vis/CLDAS_ChnTem01/.*?', '../resource/live_picture/全国小时气温实况'),
        ('http://image.data.cma.cn/vis/CLDAS_RT_CHN_0P05_HOR-VIS.*?', '../resource/live_picture/全国小时最低能见度实况'),
        ('http://image.data.cma.cn/vis/FY4A-_AGRI_L1C_TCC-_MULT_GLL_SMALL/.*?', '../resource/live_picture/卫星云量图')
    ]

    # 遍历下载图片
    for img_url_pattern, img_name in image_info:
        try:
            parr = re.compile(f'src="({img_url_pattern})"')
            images = re.findall(parr, response.text)
            # print(f'{img_name}：{images[0]}')  # 测试
            img_data = requests.get(images[0]).content
            with open(f'{img_name}.png', 'wb') as f:
                f.write(img_data)
        except:
            print(f'{img_name}下载失败')
            pass


# 下载某张图片
def download_one(flag):
    response = requests.get(url)
    # 编码一致
    response.encoding = response.apparent_encoding
    # 定义匹配链接和文件路径
    if flag == 1:
        img_url_pattern = 'http://image.data.cma.cn/vis/1kmCLDAS_ChnPre01/.*?'
        img_name = '../resource/live_picture/全国1小时累计降水量实况'
    elif flag == 2:
        # https://image.data.cma.cn/vis/1kmCLDAS_ChnPre03/20230611/1km_CMPAS_CHNPre03_china_20230611060000.png
        img_url_pattern = 'http://image.data.cma.cn/vis/1kmCLDAS_ChnPre03/.*?'
        img_name = '../resource/live_picture/全国3小时累计降水量实况'
    elif flag == 3:
        img_url_pattern = 'http://image.data.cma.cn/vis/CLDAS_ChnTem01/.*?'
        img_name = '../resource/live_picture/全国小时气温实况'
    elif flag == 4:
        img_url_pattern = 'http://image.data.cma.cn/vis/CLDAS_RT_CHN_0P05_HOR-VIS.*?'
        img_name = '../resource/live_picture/全国小时最低能见度实况'
    elif flag == 5:
        img_url_pattern = 'http://image.data.cma.cn/vis/FY4A-_AGRI_L1C_TCC-_MULT_GLL_SMALL/.*?'
        img_name = '../resource/live_picture/卫星云量图'
    else:
        return

    # 下载图片
    try:
        parr = re.compile(f'src="({img_url_pattern})"')
        images = re.findall(parr, response.text)
        # print(f'{img_name}：{images[0]}')  # 测试
        img_data = requests.get(images[0]).content
        with open(f'{img_name}.png', 'wb') as f:
            f.write(img_data)
    except:
        print(f'{img_name}下载失败')


# if __name__ == '__main__':
#     download_all()
#     download_one(2)
