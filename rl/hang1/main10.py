import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV cần vẽ
file_paths = [
    '1732696453172 - 1732696470481.csv',
    '1732696922615 - 1732696935009.csv',
    '1732697020558 - 1732697032684.csv',
    '1732697126234 - 1732697140141.csv',
    '1732697280363 - 1732697292611.csv',
    '1732697396466 - 1732697410354.csv',
    '1732697821070 - 1732697833776.csv',
    '1732697943428 - 1732697957158.csv',
    '1732698061376 - 1732698075322.csv',
    '1732698190207 - 1732698202206.csv'
]

# Tạo một cửa sổ vẽ đồ thị lớn
plt.figure(figsize=(15, 30))

# Lặp qua các file CSV
for i, file_path in enumerate(file_paths):
    data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

    # Tạo đồ thị con cho mỗi file
    plt.subplot(5, 2, i + 1)  # Tạo 5 hàng, 2 cột, vị trí thứ i+1
    columns_to_plot = ['b', 'c', 'd', 'e', 'f']
    for col in columns_to_plot:
        plt.plot(data['a'], data[col], label=col)

    # Tuỳ chỉnh giới hạn trục y và nhãn trục
    plt.ylim(0, 2500)  # Giới hạn trục y
    plt.title(f'Plot of {file_path}', fontsize=10)
    plt.xlabel('Time (a)', fontsize=8)
    plt.ylabel('Values', fontsize=8)
    plt.grid(True)
    plt.legend()

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
