import pandas as pd
import matplotlib.pyplot as plt
import os

# Danh sách file CSV mới
file_paths = [
    '1733205484022 - 1733205495134.csv',
    '1733205721564 - 1733205732828.csv',
    '1733205869306 - 1733205880858.csv',
    '1733205983142 - 1733205994504.csv',
    '1733206095302 - 1733206108418.csv',
    '1733206196906 - 1733206208305.csv',
    '1733206297955 - 1733206309340.csv',
    '1733206409766 - 1733206420881.csv',
    '1733206549293 - 1733206559195.csv',
    '1733206674379 - 1733206685739.csv'
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
