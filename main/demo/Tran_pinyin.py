import pandas as pd


# 天气后报
# 城市名查找拼音
def find_tqhb_py(city_CN):
    try:
        file_name = '../resource/file/tqhb.xlsx'
        df = pd.read_excel(file_name, index_col=None)
        # 使用loc定位
        row = df.loc[df['City_CN'] == city_CN]
        result = row.values[0][1]
        return result
    except:
        print('查找不到该城市')


# 天气史
# 城市名查找拼音
def find_tqs_py(city_CN):
    try:
        file_name = '../resource/file/tqs.xlsx'
        df = pd.read_excel(file_name, index_col=None)
        # 使用loc定位
        row = df.loc[df['City_CN'] == city_CN]
        result = row.values[0][1]
        return result
    except:
        print('查找不到该城市')


# if __name__ == '__main__':
#     print(find_tqhb_py('北京'))
#     print(find_tqs_py('北京'))
