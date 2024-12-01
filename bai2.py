import sympy as sym
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
import pandas as pd
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    choice = choice_var.get()
    if filepath:
        df = pd.read_csv(filepath)
        for i in range (0,len(df)):
            # Chuyển đổi biểu thức thành dạng SymPy
            x = sym.symbols('x')  # Giả định biến là x
            expr_sympy = sym.sympify(df['pt'][i])
            print(expr_sympy)
            # Xử lý từng lựa chọn
            if choice == '1':  # Đạo hàm
                result = sym.diff(expr_sympy, x)
                df['kq dao ham'][i] = result
                
            elif choice == '2':  # Tích phân
                result = sym.integrate(expr_sympy, x)
                df['kq tich phan'][i] = result
            elif choice == '3':  # Tìm giới hạn (lim)
                result = sym.limit(expr_sympy, x, sym.oo)  # Tính lim khi x -> ∞
                df['kq lim'][i] = result
            elif choice == '4':  # Khai triển phương trình
                result = sym.series(expr_sympy, x)
                df['kq khai trien pt'][i] = result
            elif choice == '5':  # Rút gọn phương trình
                result = sym.simplify(expr_sympy)
                df['kq rut gon pt'][i] = result
            elif choice == '6':  # Giải phương trình
                result = sym.solve(expr_sympy, x)
                df['kq giai pt'][i] = result
            else:
                result = "Lựa chọn không hợp lệ"
            df.to_csv(filepath,index=False)
            # Hiển thị kết quả
            messagebox.showinfo("Kết quả", f"Kết quả: {result}")

            # Gọi hàm vẽ đồ thị
            plot_graph(expr_sympy)




# Hàm xử lý xác nhận khi người dùng nhấn nút
def handle_confirm():
    # Nhận lựa chọn của người dùng
    choice = choice_var.get()
    expr = id_entry.get()  # Lấy phương trình đầu vào từ Entry
    subject = subject_entry.get()  # Lấy tên môn học (nếu có)
    if not expr:
        messagebox.showerror("Lỗi", "Vui lòng nhập phương trình")
        return

    try:
        # Chuyển đổi biểu thức thành dạng SymPy
        x = sym.symbols('x')  # Giả định biến là x
        expr_sympy = sym.sympify(expr)

        # Xử lý từng lựa chọn
        if choice == '1':  # Đạo hàm
            result = sym.diff(expr_sympy, x)
        elif choice == '2':  # Tích phân
            result = sym.integrate(expr_sympy, x)
        elif choice == '3':  # Tìm giới hạn (lim)
            result = sym.limit(expr_sympy, x, sym.oo)  # Tính lim khi x -> ∞
        elif choice == '4':  # Khai triển phương trình
            result = sym.series(expr_sympy, x)
        elif choice == '5':  # Rút gọn phương trình
            result = sym.simplify(expr_sympy)
        elif choice == '6':  # Giải phương trình
            result = sym.solve(expr_sympy, x)
        else:
            result = "Lựa chọn không hợp lệ"
        
        # Hiển thị kết quả
        messagebox.showinfo("Kết quả", f"Kết quả: {result}")

        # Gọi hàm vẽ đồ thị
        plot_graph(expr_sympy)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

# Hàm vẽ đồ thị của hàm số
def plot_graph(expr):
    x = sym.symbols('x')
    f_lambdified = sym.lambdify(x, expr, 'numpy')  # Chuyển đổi biểu thức SymPy thành hàm để tính toán
    x_vals = np.linspace(-10, 10, 400)  # Tạo giá trị x từ -10 đến 10
    y_vals = f_lambdified(x_vals)  # Tính giá trị y từ hàm f(x)

    plt.plot(x_vals, y_vals, label=f'y = {expr}')  # Vẽ biểu đồ hàm số
    plt.axhline(0, color='black',linewidth=0.5)  # Vẽ trục x
    plt.axvline(0, color='black',linewidth=0.5)  # Vẽ trục y
    plt.title('Đồ thị hàm số')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ứng dụng môn giải tích")

    # Thêm các widget
    tk.Label(root, text="Chọn hành động:").pack(pady=5)

    global choice_var
    choice_var = tk.StringVar(value='1')

    tk.Radiobutton(root, text="Đạo hàm", variable=choice_var, value='1').pack(anchor='w')
    tk.Radiobutton(root, text="Tích phân", variable=choice_var, value='2').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm lim", variable=choice_var, value='3').pack(anchor='w')
    tk.Radiobutton(root, text="Khai triển phương trình", variable=choice_var, value='4').pack(anchor='w')
    tk.Radiobutton(root, text="Rút gọn phương trình", variable=choice_var, value='5').pack(anchor='w')
    tk.Radiobutton(root, text="Giải phương trình", variable=choice_var, value='6').pack(anchor='w')

    tk.Label(root, text="Nhập phương trình:").pack(pady=5)
    
    global id_entry
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    tk.Label(root, text="Tên môn học (nếu có):").pack(pady=5)
    
    global subject_entry
    subject_entry = tk.Entry(root)
    subject_entry.pack(pady=5)

    tk.Button(root, text="Xác nhận", command=handle_confirm).pack(pady=10)
    # Nút để chọn tệp
    button = tk.Button(root, text="Chọn tệp CSV", command=open_file)
    button.pack(pady=20)
    root.mainloop()
    


if __name__ == "__main__":
    main()
