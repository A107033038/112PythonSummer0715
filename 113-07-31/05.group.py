import requests

#IMG = ''
IMG = 'https://thecinemaarchives.com/wp-content/uploads/2023/01/adjani-alkjdflja-e1673901309207.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer iXp6jDX3miPqQpQBnCa4rSlDR7XWnVc9LfxkLtQymhC'
P['message'] = '群組網路圖片'
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)