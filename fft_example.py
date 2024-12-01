import numpy as np
import matplotlib.pyplot as plotter
import tkinter as tk
from tkinter import simpledialog,filedialog
import pandas as pd
def run_filter():
    option = float(simpledialog.askstring("Input", "Chon cach nhap du lieu (1:tu file ,2:tu giao dien nhap)",initialvalue="1"))
    if option==2:
        # Lấy giá trị tần số từ người dùng
        signal1Frequency = float(simpledialog.askstring("Input", "Nhập tần số của tín hiệu 1 (Hz):", initialvalue="4"))
        signal2Frequency = float(simpledialog.askstring("Input", "Nhập tần số của tín hiệu 2 (Hz):", initialvalue="7"))
        cutoff = float(simpledialog.askstring("Input", "Nhập tần số cắt (Hz):", initialvalue="7"))
    elif option==1:
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            df = pd.read_csv(filepath)
            signal1Frequency=float(df['Thong1'])
            signal2Frequency = float(df['Thong2'])
            cutoff=float(df['Tansocat'])
        
        


    # Các thông số cần thiết
    samplingFrequency = 100
    samplingInterval = 1 / samplingFrequency
    beginTime = 0
    endTime = 10

    # Tạo các điểm thời gian
    time = np.arange(beginTime, endTime, samplingInterval)

    # Tạo 2 sóng sin
    amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
    amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

    # Tổng của hai sóng sin
    amplitude = amplitude1 + amplitude2

    # Tạo đồ thị
    figure, axis = plotter.subplots(4, 1)
    plotter.subplots_adjust(hspace=1)

    # Biểu diễn thời gian của sóng sin
    axis[0].set_title(f'Sóng sin có tần số {signal1Frequency} Hz')
    axis[0].plot(time, amplitude1)
    axis[0].set_xlabel('Thời gian')
    axis[0].set_ylabel('Biên độ')

    axis[1].set_title(f'Sóng sin có tần số {signal2Frequency} Hz')
    axis[1].plot(time, amplitude2)
    axis[1].set_xlabel('Thời gian')
    axis[1].set_ylabel('Biên độ')

    # Sóng kết hợp (miền thời gian)
    axis[2].set_title(f'Sóng kết hợp ({signal1Frequency} Hz + {signal2Frequency} Hz)')
    axis[2].plot(time, amplitude)
    axis[2].set_xlabel('Thời gian')
    axis[2].set_ylabel('Biên độ')

    # Miền tần số (Fourier Transform)
    fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Chuẩn hóa biên độ
    frequencies = np.fft.fftfreq(len(amplitude), d=samplingInterval)
    if cutoff<signal2Frequency:
        fourierTransform[np.abs(frequencies) > cutoff] = 0
    else:
        # Bộ lọc thông cao: loại bỏ các tần số dưới giá trị cutoff
        fourierTransform[np.abs(frequencies) < cutoff] = 0

    # Inverse FFT để lấy lại tín hiệu đã lọc trong miền thời gian
    filtered_amplitude = np.fft.ifft(fourierTransform * len(amplitude))

    # Vẽ miền tần số sau khi áp dụng bộ lọc
    axis[3].set_title(f'Fourier Transform sau lọc (Thông cao {cutoff}Hz)')
    axis[3].plot(frequencies[:len(frequencies)//2], np.abs(fourierTransform[:len(fourierTransform)//2]))
    axis[3].set_xlabel('Tần số')
    axis[3].set_ylabel('Biên độ')

    plotter.show()

# Tạo giao diện chính với Tkinter
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính

# Hiển thị cửa sổ nhập liệu
run_filter()
