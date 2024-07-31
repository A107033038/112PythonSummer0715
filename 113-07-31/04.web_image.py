import requests

#IMG = ''
IMG = 'https://indie-outlook.com/wp-content/uploads/2021/06/enter-the-void-header.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer xYKjZviTa2z1EWYc6NvGMnXZJRZ9ABKJhkYHWDaNB10'
P['message'] = '本機圖片'
F['imageFile'] = requests.get(IMG).content
requests.post(URL, headers=H, params=P, files=F)