import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Hàm để chọn tệp và đọc dữ liệu CSV
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        df = pd.read_csv(filepath)
        # Lấy dữ liệu tam giác từ file CSV
        a = df['a'][0]
        b = df['b'][0]
        c = df['c'][0]
        
        # Kiểm tra xem 3 cạnh có hợp lệ để tạo thành tam giác không
        if a + b > c and a + c > b and b + c > a:
            plot_triangle(a, b, c)
        else:
            print("Các cạnh đã nhập không hợp lệ để tạo thành tam giác.")

# Hàm vẽ tam giác
def plot_triangle(a, b, c):
    # Tọa độ đỉnh tam giác
    x1, y1 = 0, 0
    x2, y2 = a, 0
    x3 = (a**2 + c**2 - b**2) / (2 * a)
    y3 = (c**2 - x3**2)**0.5

    # Vẽ tam giác
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'b')
    plt.title(f'Tam giác với các cạnh a={a}, b={b}, c={c}')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Tạo giao diện chính
root = tk.Tk()
root.title("Chọn tệp CSV")
root.geometry("300x100")

# Nút để chọn tệp
button = tk.Button(root, text="Chọn tệp CSV", command=open_file)
button.pack(pady=20)

# Bắt đầu vòng lặp giao diện
root.mainloop()