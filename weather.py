#!/usr/bin/env python3
import json
import urllib.request
import os,time

city = 'wuhan'


def get_json(city):
    url = 'https://free-api.heweather.com/s6/weather/now?location=wuhan&key=01fabac8d743432ba352382f9cab7fd3 '
    html = urllib.request.urlopen(url).read()  # get请求打开指定url
    return html


# 调用api端口获取city的天气实况
data = get_json(city)
# print(data.decode())#解码获取到的参数并输出
hjson = json.loads(data.decode('utf-8'))  # 解析获取的信息
basic_status = hjson['HeWeather6'][0]['basic']
nowtq_status = hjson['HeWeather6'][0]['now']
# print(hjson)

# 获取国家和地区


def basic(databasic):
    # print('国家/城市名称:%s/%s' % (databasic['cnty'], databasic['location']))
    pass

basic(basic_status)

# 获取实况天气


def now(datanowtq):
   
    skydata0 = ('体感温度:%s度' % (datanowtq['fl']))
    skydata0 += (' 温度:%s度' % (datanowtq['tmp']))
    #yield skydata
    skydata1 = (' 天气:%s' % (datanowtq['cond_txt']))
    skydata1 += (' 风向:%s' % (datanowtq['wind_dir']))
    #yield skydata1
    skydata2 = ('风力:%s级' % (datanowtq['wind_sc']))
    skydata2 += (' 风速:%s公里/小时' % (datanowtq['wind_spd']))
    #yield skydata2
    skydata3 = (' 相对湿度:%s' % (datanowtq['hum']))
    skydata3 += (' 降水量:%s' % (datanowtq['pcpn']))
    #yield skydata3
    skydata4 = (' 大气压强:%s' % (datanowtq['pres']))
    skydata4 += (' 能见度:%s公里' % (datanowtq['vis']))
    # l = [skydata,skydata1,skydata2,skydata3,skydata4]
    #yield skydata4
    skydata = skydata0 + skydata1 + "\n" + skydata2 +\
    skydata3 + "\n" + skydata4
    return skydata 


    
now(nowtq_status)

