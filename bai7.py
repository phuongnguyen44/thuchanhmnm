import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
if filepath:
    df = pd.read_csv(filepath, encoding='latin1')
    messagebox.showinfo("Load Data", "Data loaded successfully!")
else:
    messagebox.showwarning("Load Data", "No file selected.")

# Bước 2: Xử lý dữ liệu bị thiếu
df = df.dropna()  # Loại bỏ các hàng có giá trị thiếu

# Bước 3: Tách dữ liệu thành đặc trưng (X) và nhãn (y)
X = df.drop('Potability', axis=1)
y = df['Potability']

# Bước 4: Chia dữ liệu thành tập huấn luyện và kiểm tra (80% huấn luyện, 20% kiểm tra)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bước 5: Huấn luyện mô hình với RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Bước 6: Dự đoán trên tập kiểm tra và đánh giá mô hình
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Tạo giao diện với Tkinter
def predict_water_quality():
    try:
        # Lấy giá trị đầu vào từ người dùng
        ph_value = float(entry_ph.get())
        hardness = float(entry_hardness.get())
        solids = float(entry_solids.get())
        chloramines = float(entry_chloramines.get())
        sulfate = float(entry_sulfate.get())
        conductivity = float(entry_conductivity.get())
        organic_carbon = float(entry_organic_carbon.get())
        trihalomethanes = float(entry_trihalomethanes.get())
        turbidity = float(entry_turbidity.get())

        # Chuẩn bị dữ liệu cho dự đoán
        input_data = [[ph_value, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]
        
        # Dự đoán với mô hình đã huấn luyện
        prediction = rf_model.predict(input_data)
        result = "Nước đạt tiêu chuẩn uống được" if prediction == 1 else "Nước không đạt tiêu chuẩn"
        messagebox.showinfo("Kết quả dự đoán", result)

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Dự đoán chất lượng nước")

# Các thành phần giao diện nhập liệu
tk.Label(root, text="pH:").grid(row=0, column=0)
entry_ph = tk.Entry(root)
entry_ph.grid(row=0, column=1)

tk.Label(root, text="Hardness:").grid(row=1, column=0)
entry_hardness = tk.Entry(root)
entry_hardness.grid(row=1, column=1)

tk.Label(root, text="Solids:").grid(row=2, column=0)
entry_solids = tk.Entry(root)
entry_solids.grid(row=2, column=1)

tk.Label(root, text="Chloramines:").grid(row=3, column=0)
entry_chloramines = tk.Entry(root)
entry_chloramines.grid(row=3, column=1)

tk.Label(root, text="Sulfate:").grid(row=4, column=0)
entry_sulfate = tk.Entry(root)
entry_sulfate.grid(row=4, column=1)

tk.Label(root, text="Conductivity:").grid(row=5, column=0)
entry_conductivity = tk.Entry(root)
entry_conductivity.grid(row=5, column=1)

tk.Label(root, text="Organic Carbon:").grid(row=6, column=0)
entry_organic_carbon = tk.Entry(root)
entry_organic_carbon.grid(row=6, column=1)

tk.Label(root, text="Trihalomethanes:").grid(row=7, column=0)
entry_trihalomethanes = tk.Entry(root)
entry_trihalomethanes.grid(row=7, column=1)

tk.Label(root, text="Turbidity:").grid(row=8, column=0)
entry_turbidity = tk.Entry(root)
entry_turbidity.grid(row=8, column=1)

# Nút để dự đoán
tk.Button(root, text="Dự đoán", command=predict_water_quality).grid(row=9, column=0, columnspan=2)

# Bắt đầu giao diện
root.mainloop()
