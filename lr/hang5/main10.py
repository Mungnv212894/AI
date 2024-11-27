import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV cần vẽ
file_paths = [
    '1732603330706 - 1732603341696.csv',
    '1732604259320 - 1732604270142.csv',
    '1732603466489 - 1732603477232.csv',
    '1732604302421 - 1732604314079.csv',
    '1732603558835 - 1732603569670.csv',
    '1732604664517 - 1732604675003.csv',
    '1732603601165 - 1732603611971.csv',
    '1732604684991 - 1732604695458.csv',
    '1732604222214 - 1732604232229.csv',
    '1732604240895 - 1732604251893.csv'
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
