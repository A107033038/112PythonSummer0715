import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-2833E920-9156-4169-B0FE-D8A6BD0848C0'
r = requests.get(URL, params=P)
t = r.json()

location = input('查詢地點：')
n = len(t['records']['Station'])
found = False
for i in range(n):
    if t['records']['Station'][i]['StationName'] == location:
        print('觀測地點：', t['records']['Station'][i]['StationName'])
        print('觀測地點編號：', i)
        print('觀測時間：', t['records']['Station'][i]['ObsTime']['DateTime'])
        print('觀測溫度：', t['records']['Station'][i]['WeatherElement']['AirTemperature'])
        print('觀測濕度：', t['records']['Station'][i]['WeatherElement']['RelativeHumidity'])
        print('觀測天氣：', t['records']['Station'][i]['WeatherElement']['Weather'])
        found = True
        break

if (found == False):
    print('輸入站點不存在')