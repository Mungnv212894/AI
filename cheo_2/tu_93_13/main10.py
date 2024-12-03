import pandas as pd
import matplotlib.pyplot as plt
import os

# Danh sách file CSV cập nhật
file_paths = [
    '1733198157013 - 1733198170362.csv',
    '1733198265076 - 1733198278920.csv',
    '1733198381164 - 1733198392614.csv',
    '1733198489211 - 1733198512628.csv',
    '1733198633340 - 1733198645106.csv',
    '1733198731815 - 1733198743928.csv',
    '1733198851619 - 1733198867971.csv',
    '1733199021003 - 1733199038352.csv',
    '1733199127040 - 1733199138853.csv',
    '1733199237769 - 1733199256944.csv'
]

# Kiểm tra file tồn tại
existing_files = [file for file in file_paths if os.path.exists(file)]
if not existing_files:
    print("No valid files found. Check file paths!")
    exit()

# Thiết lập kích thước đồ thị
plt.figure(figsize=(15, 30))

# Lặp qua từng file để vẽ đồ thị
for i, file_path in enumerate(existing_files):
    try:
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

        # Kiểm tra nếu file trống
        if data.empty:
            print(f"File {file_path} is empty. Skipping...")
            continue

        # Tạo đồ thị con
        plt.subplot(6, 2, i + 1)  # Tối đa 12 đồ thị
        columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột để vẽ

        # Vẽ dữ liệu
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

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
