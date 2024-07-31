import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer xYKjZviTa2z1EWYc6NvGMnXZJRZ9ABKJhkYHWDaNB10'
P['message'] = '本機圖片'
#F['imageFile'] = open(r'C:\Users\m303\Documents\GitHub\112PythonSummer0715\Kairo.jpg','rb')  #絕對路徑
#F['imageFile'] = open('Possession_still_02.jpg','rb')
F['imageFile'] = open('./pictures/Dressed_to_Kill.jpg','rb')
requests.post(URL, headers=H, params=P, files=F)