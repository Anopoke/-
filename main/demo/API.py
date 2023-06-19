import requests


# 腾讯位置服务 获取定位
def location_query():
    # https://apis.map.qq.com/ws/location/v1/ip?key=NR2BZ-NQMCH-ALNDJ-W6NQA-VOROZ-CBBY7
    url = 'https://apis.map.qq.com/ws/location/v1/ip'
    key = 'NR2BZ-NQMCH-ALNDJ-W6NQA-VOROZ-CBBY7'
    params = {'key': key}
    response = requests.get(url, params)
    rs = response.json()
    result = rs['result']['ad_info']
    city0 = result['city'].strip('市')
    # 查看能否获取到区级
    if result['district'] == '':
        data = {'city0': city0, 'city': city0, 'adcode': result['adcode']}
    else:
        data = {'city0': city0, 'city': result['district'], 'adcode': result['adcode']}
    return data


# 高德地图 live_picture
# 传入参数：城市编码
def live_weather(adcode):
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    key = '79ebdfdc68b119a9cdeb8de28c413978'
    extensions = 'base'
    params = {'key': key, "city": adcode, 'extensions': extensions}
    response = requests.get(url, params)
    info = response.json()
    result = info['lives'][0]
    return result


# 高德地图 预报天气
# 传入参数：城市编码
def forecast_weather(adcode):
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    key = '79ebdfdc68b119a9cdeb8de28c413978'
    extensions = 'all'
    params = {'key': key, "city": adcode, 'extensions': extensions}
    response = requests.get(url, params)
    info = response.json()
    result = info['forecasts'][0]
    return result


# 心知天气 生活指标
# 传入参数：城市中文名
def target(city):
    url = 'https://api.seniverse.com/v3/life/suggestion.json'
    key = 'SjMPR7fzKw56y0UT7'
    params = {'key': key, 'location': city, 'days': 1}
    response = requests.get(url=url, params=params)
    a = dict(response.json())
    b = a['results'][0]['suggestion'][0]
    # 最后更新时间
    reflush_data = a['results'][0]['last_update']
    # 各项指标
    uv = b['uv']
    dressing = b['dressing']
    umbrella = b['umbrella']
    flu = b['flu']
    sport = b['sport']
    car_washing = b['car_washing']
    result = {'紫外线': uv, '穿衣': dressing, '运动': sport, '雨伞': umbrella, '感冒': flu, '洗车': car_washing,
              '时间': reflush_data}
    return result


# if __name__ == '__main__':
#     loc = location_query()
#     print(loc)
#     print(live_weather(adcode=loc['adcode']))
#     print(forecast_weather(adcode=loc['adcode']))
#     print(location_query())
#     print(target(loc['city0']))
