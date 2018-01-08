import requests
import re
import pandas as pd
import time,random
#真是网址
url = 'http://hotel.elong.com/beijing/'
#反爬措施
header = {
    ' Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'1601',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'hotel.elong.com',
    'Origin':'http://hotel.elong.com',
    'Referer:http':'//hotel.elong.com/beijing/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.1.1.16851',
    'X-Requested-With':'XMLHttpRequest',
    }


det = {
    'code':'9328199',
    'listRequest.areaID':'',
    'listRequest.bookingChannel':'5',
    'listRequest.cardNo':'192928',
    'listRequest.checkInDate':'2018-01-05 00:00:00',
    'listRequest.checkOutDate':'2018-01-06 00:00:00',
    'listRequest.cityID':'0101',
    'listRequest.cityName':'北京市',
    'listRequest.customLevel':'11',
    'listRequest.distance':'20',
    'listRequest.endLat':'0',
    'listRequest.endLng':'0',
    'listRequest.facilityIds':'',
    'listRequest.highPrice':'0',
    'listRequest.hotelBrandIDs':'',
    'listRequest.isAdvanceSave':'false',
    'listRequest.isAfterCouponPrice':'true',
    'listRequest.isCoupon':'false',
    'listRequest.isDebug':'false',
    'listRequest.isLimitTime':'false',
    'listRequest.isLogin':'false',
    'listRequest.isMobileOnly':'true',
    'listRequest.isNeed5Discount':'true',
    'listRequest.isNeedNotContractedHotel':'false',
    'listRequest.isNeedSimilarPrice':'false',
    'listRequest.isReturnNoRoomHotel':'true',
    'listRequest.isStaySave':'false',
    'listRequest.isTrace':'false',
    'listRequest.isUnionSite':'false',
    'listRequest.keywords':'',
    'listRequest.keywordsType':'0',
    'listRequest.language':'cn',
    'listRequest.listType':'0',
    'listRequest.lowPrice':'0',
    'listRequest.orderFromID':'1003',
    'listRequest.pageIndex':'6',#翻页
    'listRequest.pageSize':'20',
    'listRequest.payMethod':'0',
    'listRequest.personOfRoom':'0',
    'listRequest.poiId':'0',
    'listRequest.promotionChannelCode':'0000',
    'listRequest.proxyID':'ZD',
    'listRequest.rankType':'0',
    'listRequest.returnFilterItem':'true',
    'listRequest.sellChannel':'1',
    'listRequest.seoHotelStar':'0',
    'listRequest.sortDirection':'1',
    'listRequest.sortMethod':'1',
    'listRequest.starLevels':'',
    'listRequest.startLat':'0',
    'listRequest.startLng':'0'
    'listRequest.taRecommend:false',
    'listRequest.themeIds':'',
    'listRequest.ctripToken':'e650c33e-2d15-4258-9df3-ffa3ac47639c',
    'listRequest.elongToken':'jc0i3dcc-e023-47e5-a677-7c00f3e50e4c',
    }
#提交数据给服务器         headers=header  反爬措施（告诉浏览器我们是用浏览器请求的数据）
html = requests.post(url,data = det,headers = header)
html.json()
#正则表达式
hotel_pri = re.findall('class="h_pri_num">(.*?)</span>',html.json())
hotel_name = re.findall('class="h_pri_num">(.*?)</span>',html.json())

data = list(map(lambda x:(hotme_name[x],hotel_pri[x]),range(len(htel_name))))
data2 = pd.DataFrame(data)#数据框
#保存样式（csv）mode=‘a+’ 是追加格式   (写入本地data2.to_csv('路径',header=False,index=False,mode='a+'))
data2.to_csv(r'c:\Users\Administrator\Desktop\yilong.csv.',header=False,index=False,mode='a+')

#提取头部数据  输出data2  data2.loc[0:1,:] 



for n in range(1,10):
    dat = {
        'code':'9328199',
    'listRequest.areaID':'',
    'listRequest.bookingChannel':'5',
    'listRequest.cardNo':'192928',
    'listRequest.checkInDate':'2018-01-05 00:00:00',
    'listRequest.checkOutDate':'2018-01-06 00:00:00',
    'listRequest.cityID':'0101',
    'listRequest.cityName':'北京市',
    'listRequest.customLevel':'11',
    'listRequest.distance':'20',
    'listRequest.endLat':'0',
    'listRequest.endLng':'0',
    'listRequest.facilityIds':'',
    'listRequest.highPrice':'0',
    'listRequest.hotelBrandIDs':'',
    'listRequest.isAdvanceSave':'false',
    'listRequest.isAfterCouponPrice':'true',
    'listRequest.isCoupon':'false',
    'listRequest.isDebug':'false',
    'listRequest.isLimitTime':'false',
    'listRequest.isLogin':'false',
    'listRequest.isMobileOnly':'true',
    'listRequest.isNeed5Discount':'true',
    'listRequest.isNeedNotContractedHotel':'false',
    'listRequest.isNeedSimilarPrice':'false',
    'listRequest.isReturnNoRoomHotel':'true',
    'listRequest.isStaySave':'false',
    'listRequest.isTrace':'false',
    'listRequest.isUnionSite':'false',
    'listRequest.keywords':'',
    'listRequest.keywordsType':'0',
    'listRequest.language':'cn',
    'listRequest.listType':'0',
    'listRequest.lowPrice':'0',
    'listRequest.orderFromID':'1003',
    'listRequest.pageIndex':str(n),#翻页
    'listRequest.pageSize':'20',
    'listRequest.payMethod':'0',
    'listRequest.personOfRoom':'0',
    'listRequest.poiId':'0',
    'listRequest.promotionChannelCode':'0000',
    'listRequest.proxyID':'ZD',
    'listRequest.rankType':'0',
    'listRequest.returnFilterItem':'true',
    'listRequest.sellChannel':'1',
    'listRequest.seoHotelStar':'0',
    'listRequest.sortDirection':'1',
    'listRequest.sortMethod':'1',
    'listRequest.starLevels':'',
    'listRequest.startLat':'0',
    'listRequest.startLng':'0'
    'listRequest.taRecommend:false',
    'listRequest.themeIds':'',
    'listRequest.ctripToken':'e650c33e-2d15-4258-9df3-ffa3ac47639c',
    'listRequest.elongToken':'jc0i3dcc-e023-47e5-a677-7c00f3e50e4c',
        }
    #提交数据给服务器
    html = requests.post(url,data = dat,headers = header)
    hotel_pri = re.findall('class="h_pri_num">(.*?)</span>',html.json())
    hotel_name = re.findall('class="h_pri_num">(.*?)</span>',html.json())
    data = list(map(lambda x:(hotme_name[x],hotel_pri[x]),range(len(htel_name))))
    data2 = pd.DataFrame(data)
    data2.to_csv(r'c:\Users\Administrator\Desktop\yilong.csv.',header=False,index=False,mode='a+')
    #暂停几秒后执行
    time.sleep(random.randint(1,5))


















