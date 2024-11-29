import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732849111925 - 1732849126464.csv',
    '1732849214986 - 1732849222824.csv',
    '1732850583316 - 1732850591401.csv',
    '1732849484333 - 1732849492744.csv',
    '1732849585929 - 1732849593653.csv',
    '1732849695461 - 1732849704249.csv',
    '1732849869187 - 1732849885586.csv',
    '1732850027571 - 1732850034048.csv',
    '1732850121595 - 1732850130065.csv',
    '1732850226604 - 1732850234256.csv'
]

# Kích thước cửa sổ đồ thị
plt.figure(figsize=(15, 28))

# Lặp qua từng file CSV và vẽ đồ thị
for i, file_path in enumerate(file_paths):
    try:
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])
        
        # Kiểm tra nếu file rỗng
        if data.empty:
            print(f"File {file_path} is empty. Skipping...")
            continue

        # Tạo đồ thị con cho mỗi file
        plt.subplot(5, 2, i + 1)  # 5 hàng, 2 cột (hiển thị 10 đồ thị), vị trí thứ i+1
        columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột cần vẽ
        
        # Vẽ các cột
        for col in columns_to_plot:
            if col in data:
                plt.plot(data['a'], data[col], label=col)

        # Cài đặt hiển thị cho đồ thị
        plt.ylim(0, 2500)  # Giới hạn trục y
        plt.title(f'Plot of {file_path}', fontsize=10)
        plt.xlabel('Time (a)', fontsize=8)
        plt.ylabel('Values', fontsize=8)
        plt.grid(True)
        plt.legend()

    except FileNotFoundError:
        print(f"File {file_path} not found. Skipping...")
    except pd.errors.EmptyDataError:
        print(f"File {file_path} is empty or corrupted. Skipping...")
    except Exception as e:
        print(f"An error occurred with file {file_path}: {e}")

# Hiển thị tất cả đồ thị
plt.tight_layout()
plt.show()