import pandas as pd
import matplotlib.pyplot as plt
import os

# Danh sách file CSV cập nhật
file_paths = [
    '1733199885264 - 1733199894943.csv',
    '1733199995039 - 1733200007020.csv',
    '1733200088957 - 1733200100647.csv',
    '1733200188922 - 1733200199948.csv',
    '1733200414266 - 1733200426513.csv',
    '1733200505595 - 1733200514981.csv',
    '1733200581303 - 1733200592340.csv',
    '1733200652696 - 1733200662494.csv',
    '1733200717762 - 1733200728245.csv',
    '1733200792383 - 1733200803964.csv'
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
