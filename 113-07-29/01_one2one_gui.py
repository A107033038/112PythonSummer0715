import tkinter as tk
import requests

# 定義發送消息的函數
def send_message():
    token = token_entry.get()  # 獲取輸入的訪問令牌
    message = message_entry.get()  # 獲取輸入的訊息
    if token and message:
        headers = {
            'Authorization': f'Bearer {token}'  # 使用輸入的訪問令牌
        }
        data = {
            'message': message
        }
        response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
        if response.status_code == 200:
            result_label.config(text="訊息已發送！")
        else:
            result_label.config(text="發送失敗，請檢查訪問令牌或訊息格式。")
    else:
        result_label.config(text="請輸入訪問令牌和訊息！")

# 建立 GUI 視窗
root = tk.Tk()
root.title("LINE Notify")

# 訪問令牌輸入框
token_label = tk.Label(root, text="請輸入權杖:")
token_label.pack(pady=10)
token_entry = tk.Entry(root, width=50, show="*")  # 使用星號隱藏輸入的訪問令牌
token_entry.pack(pady=10)

# 訊息輸入框
message_label = tk.Label(root, text="請輸入訊息:")
message_label.pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

# 發送按鈕
send_button = tk.Button(root, text="送出", command=send_message)
send_button.pack(pady=10)

# 結果顯示標籤
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# 開始主循環
root.mainloop()
