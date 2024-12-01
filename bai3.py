import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import filedialog
import pandas as pd
import numpy as np

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        df = pd.read_csv(filepath)    
        if(len(df.columns) ==3):
            # Lấy dữ liệu tam giác từ file CSV
            a = df['a'][0]
            b = df['b'][0]
            c = df['c'][0]

            # Kiểm tra xem 3 cạnh có hợp lệ để tạo thành tam giác không
            if a + b > c and a + c > b and b + c > a:
                plot_triangle(a, b, c)
            else:
                print("Các cạnh đã nhập không hợp lệ để tạo thành tam giác.")
        elif (len(df.columns) ==1):
            a = df['a'][0]
            plot_square(a)
        elif (len(df.columns)==2):
            a = df['a'][0]
            b = df['b'][0]
            plot_rectangle(a, b)

def draw_shape():
    shape = shape_var.get()
    
    if shape == "Tam giác":
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            if a + b > c and a + c > b and b + c > a:  # Điều kiện tam giác
                plot_triangle(a, b, c)
            else:
                messagebox.showerror("Lỗi", "Không hợp lệ: Tổng hai cạnh phải lớn hơn cạnh còn lại.")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    elif shape == "Hình vuông":
        try:
            side = float(entry_a.get())
            plot_square(side)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    elif shape == "Hình chữ nhật":
        try:
            width = float(entry_a.get())
            height = float(entry_b.get())
            plot_rectangle(width, height)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def plot_triangle(a, b, c):
    plt.title('Hình tam giac')
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    C = np.arccos(cos_C) 

    # Tọa độ điểm A là (0, 0)
    A = (0, 0)

    # Tọa độ điểm B là (a, 0) vì nằm trên trục x
    B = (a, 0)

    # Tọa độ điểm C được tính từ góc C
    C_x = b * np.cos(C)  # Tọa độ x của điểm C
    C_y = b * np.sin(C)  # Tọa độ y của điểm C
    C = (C_x, C_y)

    # Vẽ tam giác
    plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-o')

    # Cài đặt trục x và y có cùng tỷ lệ để tam giác không bị méo
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


def plot_square(side):
    # Vẽ hình vuông
    plt.figure()
    plt.plot([0, side, side, 0, 0], [0, 0, side, side, 0], 'g')
    plt.title('Hình vuông')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def plot_rectangle(width, height):
    # Vẽ hình chữ nhật
    plt.figure()
    plt.plot([0, width, width, 0, 0], [0, 0, height, height, 0], 'r')
    plt.title('Hình chữ nhật')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Giao diện người dùng
root = tk.Tk()
root.title("Ứng dụng Hình Học")

shape_var = tk.StringVar(value="Tam giác")

tk.Label(root, text="Chọn hình").pack()

shapes = ["Tam giác", "Hình vuông", "Hình chữ nhật"]
for shape in shapes:
    tk.Radiobutton(root, text=shape, variable=shape_var, value=shape).pack()

tk.Label(root, text="Cạnh a (hoặc cạnh hình vuông)").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Cạnh b (hoặc chiều rộng hình chữ nhật)").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Cạnh c (chỉ cho tam giác)").pack()
entry_c = tk.Entry(root)
entry_c.pack()

button = tk.Button(root, text="Vẽ", command=draw_shape)
button.pack(pady=10)

# Nút để chọn tệp
button = tk.Button(root, text="Chọn tệp CSV", command=open_file)
button.pack(pady=20)

root.mainloop()
