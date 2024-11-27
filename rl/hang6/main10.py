import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV cần vẽ
file_paths = [
    '1732703646660 - 1732703654046.csv',
    '1732703661892 - 1732703669639.csv',
    '1732703677328 - 1732703686585.csv',
    '1732703757485 - 1732703765184.csv',
    '1732704263081 - 1732704270852.csv',
    '1732704279492 - 1732704287714.csv',
    '1732704532386 - 1732704540677.csv',
    '1732704546811 - 1732704555209.csv',
    '1732704565208 - 1732704573118.csv',
    '1732704580183 - 1732704589136.csv'
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
