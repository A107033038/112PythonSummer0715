import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer xYKjZviTa2z1EWYc6NvGMnXZJRZ9ABKJhkYHWDaNB10'
P['message'] = '早安您好，要不要吃沙威瑪？'
response = requests.post(URL, headers=H, params=P)

print(response.status_code)
print(response.text)