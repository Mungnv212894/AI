import pandas as pd
import matplotlib.pyplot as plt
import os

# Danh sách file CSV mới nhất
file_paths = [
    '1733133329703 - 1733133340140.csv',
    '1733133542201 - 1733133555432.csv',
    '1733133793938 - 1733133804363.csv',
    '1733133868930 - 1733133880312.csv',
    '1733134155853 - 1733134171744.csv',
    '1733134262722 - 1733134273925.csv',
    '1733134369460 - 1733134378644.csv',
    '1733134451404 - 1733134467436.csv',
    '1733134595694 - 1733134610727.csv',
    '1733134902906 - 1733134915640.csv'
]

# Kiểm tra sự tồn tại của file CSV
existing_files = [file for file in file_paths if os.path.exists(file)]
if not existing_files:
    print("No valid files found. Check file paths!")
    exit()

# Cấu hình kích thước cửa sổ đồ thị
plt.figure(figsize=(15, 30))

# Lặp qua từng file CSV để vẽ đồ thị
for i, file_path in enumerate(existing_files):
    try:
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

        # Kiểm tra nếu file trống
        if data.empty:
            print(f"File {file_path} is empty. Skipping...")
            continue

        # Tạo đồ thị con cho mỗi file
        plt.subplot(6, 2, i + 1)  # 6 hàng, 2 cột (tối đa 12 đồ thị), vị trí thứ i+1
        columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột cần vẽ

        # Vẽ các cột dữ liệu
        for col in columns_to_plot:
            if col in data:
                plt.plot(data['a'], data[col], label=col)

        # Cấu hình đồ thị
        plt.title(f'Plot of {os.path.basename(file_path)}', fontsize=10)
        plt.xlabel('Time (a)', fontsize=8)
        plt.ylabel('Values', fontsize=8)
        plt.ylim(0, 2500)  # Giới hạn trục Y
        plt.grid(True)
        plt.legend(fontsize=8)

    except FileNotFoundError:
        print(f"File {file_path} not found. Skipping...")
    except pd.errors.EmptyDataError:
        print(f"File {file_path} is empty or corrupted. Skipping...")
    except Exception as e:
        print(f"An error occurred with file {file_path}: {e}")

# Hiển thị tất cả đồ thị
plt.tight_layout()
plt.show()
