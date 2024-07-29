import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer xYKjZviTa2z1EWYc6NvGMnXZJRZ9ABKJhkYHWDaNB10'
P['message'] = '貼圖測試'
P['stickerPackageId'] = 789
P['stickerId'] = 10855
requests.post(URL, headers=H, params=P)