import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

# Hàm chọn ảnh
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        process_image(file_path)

# Hàm tăng cường chất lượng ảnh và hiển thị kết quả
def process_image(image_path):
    # Đọc ảnh đầu vào
    image = cv2.imread(image_path)
    if image is None:
        print("Không thể mở ảnh.")
        return

    # Tăng cường chất lượng bằng cân bằng histogram
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
    enhanced_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    # Điều chỉnh độ sáng và độ tương phản
    alpha = 1.2  # Độ tương phản
    beta = 30    # Độ sáng
    adjusted_image = cv2.convertScaleAbs(enhanced_image, alpha=alpha, beta=beta)

    # Hiển thị kết quả
    images = [image, enhanced_image, adjusted_image]
    titles = ['Original Image', 'Histogram Equalized', 'Brightness & Contrast Adjusted']

    plt.figure(figsize=(12, 8))
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

# Tạo giao diện Tkinter
root = Tk()
root.title("Image Enhancement GUI")

# Nút chọn ảnh
select_button = Button(root, text="Chọn ảnh", command=open_image)
select_button.pack(pady=20)

root.geometry("300x150")
root.mainloop()
