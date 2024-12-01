import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox



# Hàm xử lý đọc file CSV
def read_csv_file():
    filepath = filedialog.askopenfilename(title="Chọn file CSV", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if filepath:
        try:
            global df
            df = pd.read_csv(filepath)
            messagebox.showinfo("Thông báo", "Đã tải dữ liệu thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")
    else:
        messagebox.showerror("Lỗi", "Không có file nào được chọn!")

# Hàm vẽ biểu đồ
def plot_graph(option):
    if df is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước!")
        return
    
    try:
        in_data = df.iloc[:, :].to_numpy()
        tongsv = in_data[:, 2]
        diemA = in_data[:, 4]
        diemBc = in_data[:, 5]

        if option == '1':  # Vẽ biểu đồ điểm A
            plt.plot(range(len(diemA)), diemA, 'r-', label="Điểm A")
            plt.plot(range(len(diemBc)), diemBc, 'g-', label="Điểm B+")
            plt.xlabel('Lớp')
            plt.ylabel('Số SV đạt điểm')
            plt.legend(loc='upper right')
            plt.show()

        elif option == '2':  # Vẽ biểu đồ tròn
            labels = ['Điểm A', 'Điểm B+', 'Điểm khác']
            sizes = [np.sum(diemA), np.sum(diemBc), np.sum(tongsv) - np.sum(diemA) - np.sum(diemBc)]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.show()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")
# Hàm xử lý khi nhấn nút xác nhận
def handle_confirm():
    try:
        # Nhận dữ liệu từ các Entry
        num_class = int(num_class_entry.get())  # Số lượng lớp
        diem_a_list = [int(entry.get()) for entry in diem_a_entries]
        diem_b_list = [int(entry.get()) for entry in diem_b_entries]

        # Vẽ biểu đồ
        plt.plot(range(num_class), diem_a_list, 'r-', label="Điểm A")
        plt.plot(range(num_class), diem_b_list, 'g-', label="Điểm B+")
        plt.xlabel('Lớp')
        plt.ylabel('Số SV đạt điểm')
        plt.legend(loc='upper right')
        plt.show()

    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho tất cả các trường!")

# Hàm tạo các trường nhập liệu
def create_entries():
    try:
        num_class = int(num_class_entry.get())  # Số lượng lớp
        for widget in frame.winfo_children():  # Xóa các widget trước đó
            widget.destroy()

        # Tạo các trường nhập liệu cho mỗi lớp
        global diem_a_entries, diem_b_entries
        diem_a_entries = []
        diem_b_entries = []

        for i in range(num_class):
            tk.Label(frame, text=f"Lớp {i+1}:").pack()
            tk.Label(frame, text="Số SV đạt điểm A:").pack()
            diem_a_entry = tk.Entry(frame)
            diem_a_entry.pack(pady=2)
            diem_a_entries.append(diem_a_entry)

            tk.Label(frame, text="Số SV đạt điểm B+:").pack()
            diem_b_entry = tk.Entry(frame)
            diem_b_entry.pack(pady=2)
            diem_b_entries.append(diem_b_entry)

    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số lớp học!")

root = tk.Tk()
root.title("Ứng dụng báo cáo học phần")

tk.Button(root, text="Tải file CSV", command=read_csv_file).pack(pady=10)
tk.Label(root, text="Số lượng lớp học:").pack(pady=5)

# Nhập số lượng lớp học
num_class_entry = tk.Entry(root)
num_class_entry.pack(pady=5)

# Nút để tạo các trường nhập dữ liệu
tk.Button(root, text="Tạo các trường nhập liệu", command=create_entries).pack(pady=10)

# Frame chứa các trường nhập liệu
frame = tk.Frame(root)
frame.pack(pady=10)

# Nút xác nhận để xử lý và hiển thị biểu đồ
tk.Button(root, text="Xác nhận và vẽ biểu đồ", command=handle_confirm).pack(pady=10)

tk.Label(root, text="Chọn hành động:").pack(pady=5)
global option_var
option_var = tk.StringVar(value='1')

tk.Radiobutton(root, text="Vẽ biểu đồ điểm A & B+", variable=option_var, value='1').pack(anchor='w')
tk.Radiobutton(root, text="Vẽ biểu đồ tròn", variable=option_var, value='2').pack(anchor='w')

tk.Button(root, text="Xác nhận", command=lambda: plot_graph(option_var.get())).pack(pady=10)

root.mainloop()

df = None  # Biến toàn cục để lưu DataFrame
