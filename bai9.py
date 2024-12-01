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

# Hàm xử lý ảnh và hiển thị kết quả
def process_image(image_path):
    # Đọc ảnh đầu vào
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Không thể mở ảnh.")
        return
    
    # Tách biên bằng các phương pháp
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_combined = cv2.sqrt(cv2.addWeighted(sobel_x**2, 1, sobel_y**2, 1, 0))

    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    canny = cv2.Canny(image, 100, 200)

    # Hiển thị kết quả
    titles = ['Original Image', 'Sobel Edge', 'Laplacian Edge', 'Canny Edge']
    images = [image, sobel_combined, laplacian, canny]

    plt.figure(figsize=(10, 8))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

# Tạo giao diện Tkinter
root = Tk()
root.title("Edge Detection GUI")

# Nút chọn ảnh
select_button = Button(root, text="Chọn ảnh", command=open_image)
select_button.pack(pady=20)

root.geometry("300x150")
root.mainloop()
