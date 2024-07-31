import requests
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# LINE Notify API URL
URL = 'https://notify-api.line.me/api/notify'

# Function to send notification
def send_notification():
    H = {'Authorization': 'Bearer iXp6jDX3miPqQpQBnCa4rSlDR7XWnVc9LfxkLtQymhC'}
    P = {}
    F = {}

    choice = option_var.get()

    if choice == 'Line Sticker':
        P['message'] = '貼圖測試'
        P['stickerPackageId'] = sticker_package_id_var.get()
        P['stickerId'] = sticker_id_var.get()
    elif choice == 'Local Image File':
        P['message'] = '本機圖片'
        file_path = file_path_var.get()
        if file_path:
            F['imageFile'] = ('image.jpg', open(file_path, 'rb'))
    elif choice == 'Web Image File':
        P['message'] = '網路圖片'
        img_url = web_img_url_var.get()
        if img_url:
            F['imageFile'] = ('image.jpg', requests.get(img_url).content)
    else:
        messagebox.showerror("Error", "Invalid option selected")
        return

    # Send the request
    response = requests.post(URL, headers=H, params=P, files=F)
    messagebox.showinfo("Response", f"Status Code: {response.status_code}\n{response.text}")

# GUI setup
root = tk.Tk()
root.title("LINE Notify Sender")

option_var = tk.StringVar()
sticker_package_id_var = tk.StringVar()
sticker_id_var = tk.StringVar()
file_path_var = tk.StringVar()
web_img_url_var = tk.StringVar()

# Option menu
ttk.Label(root, text="Choose Option:").grid(column=0, row=0, padx=10, pady=5)
option_menu = ttk.Combobox(root, textvariable=option_var, values=["Line Sticker", "Local Image File", "Web Image File"])
option_menu.grid(column=1, row=0, padx=10, pady=5)
option_menu.current(0)

# Line Sticker inputs
ttk.Label(root, text="Sticker Package ID:").grid(column=0, row=1, padx=10, pady=5)
ttk.Entry(root, textvariable=sticker_package_id_var).grid(column=1, row=1, padx=10, pady=5)
ttk.Label(root, text="Sticker ID:").grid(column=0, row=2, padx=10, pady=5)
ttk.Entry(root, textvariable=sticker_id_var).grid(column=1, row=2, padx=10, pady=5)

# Local Image File input
ttk.Label(root, text="File Path:").grid(column=0, row=3, padx=10, pady=5)
ttk.Entry(root, textvariable=file_path_var).grid(column=1, row=3, padx=10, pady=5)
ttk.Button(root, text="Browse", command=lambda: file_path_var.set(filedialog.askopenfilename())).grid(column=2, row=3, padx=10, pady=5)

# Web Image File input
ttk.Label(root, text="Web Image URL:").grid(column=0, row=4, padx=10, pady=5)
ttk.Entry(root, textvariable=web_img_url_var).grid(column=1, row=4, padx=10, pady=5)

# Send button
ttk.Button(root, text="Send", command=send_notification).grid(column=1, row=5, padx=10, pady=10)

root.mainloop()
