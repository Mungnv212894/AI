import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV cần vẽ
file_paths = [
    '1732597342654 - 1732597362661.csv',
    '1732600449923 - 1732600457454.csv',
    '1732597599601 - 1732597616545.csv',
    '1732600466800 - 1732600475073.csv',
    '1732597811048 - 1732597831248.csv',
    '1732600983768 - 1732600992328.csv',
    '1732597957430 - 1732597977679.csv',
    '1732601063430 - 1732601071868.csv',
    '1732598130043 - 1732598146893.csv',
    '1732600432885 - 1732600439844.csv'
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
