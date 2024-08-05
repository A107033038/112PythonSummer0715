import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-2833E920-9156-4169-B0FE-D8A6BD0848C0'
r = requests.get(URL, params=P)
#print(type(r))
t = r.json()
print(t)