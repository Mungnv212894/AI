import pandas as pd
import matplotlib.pyplot as plt
import os

# Danh sách file CSV mới nhất
file_paths = [
    '1733207792088 - 1733207798899.csv',
    '1733207904805 - 1733207911884.csv',
    '1733207964800 - 1733207972403.csv',
    '1733208031175 - 1733208038779.csv',
    '1733208098517 - 1733208105812.csv',
    '1733208158462 - 1733208166222.csv',
    '1733208236181 - 1733208244158.csv',
    '1733208310870 - 1733208317935.csv',
    '1733208462649 - 1733208471297.csv',
    '1733208566086 - 1733208573657.csv'
]

# Kiểm tra các file tồn tại
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
