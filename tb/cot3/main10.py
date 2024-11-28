import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732770933467 - 1732770941844.csv',
    '1732770954158 - 1732770968907.csv',
    
    '1732771440022 - 1732771448781.csv',
    '1732771484524 - 1732771493051.csv',
    '1732771906046 - 1732771921520.csv',
    '1732772046975 - 1732772061665.csv',
    '1732772222590 - 1732772231622.csv',
    '1732772260270 - 1732772268966.csv',
    '1732772665897 - 1732772673424.csv',
    '1732773125078 - 1732773134609.csv'
    
]

# Kích thước cửa sổ đồ thị
plt.figure(figsize=(15, 33))

# Lặp qua từng file CSV và vẽ đồ thị
for i, file_path in enumerate(file_paths):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

    # Tạo đồ thị con cho mỗi file
    plt.subplot(6, 2, i + 1)  # 6 hàng, 2 cột (hiển thị 11 đồ thị), vị trí thứ i+1
    columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột cần vẽ
    for col in columns_to_plot:
        plt.plot(data['a'], data[col], label=col)

    # Cài đặt hiển thị cho đồ thị
    plt.ylim(0, 2500)  # Giới hạn trục y
    plt.title(f'Plot of {file_path}', fontsize=10)
    plt.xlabel('Time (a)', fontsize=8)
    plt.ylabel('Values', fontsize=8)
    plt.grid(True)
    plt.legend()

# Hiển thị tất cả đồ thị
plt.tight_layout()
plt.show()
