import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer xYKjZviTa2z1EWYc6NvGMnXZJRZ9ABKJhkYHWDaNB10'
P['message'] = '本機圖片'
F['imageFile'] = open('Possession_still.jpg','rb')
requests.post(URL, headers=H, params=P, files=F)