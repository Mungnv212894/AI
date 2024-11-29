import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732846025079 - 1732846044895.csv',
    '1732846169784 - 1732846188424.csv',
    '1732846277933 - 1732846288618.csv',
    '1732846385861 - 1732846404638.csv',
    '1732846487157 - 1732846501437.csv',
    '1732846608702 - 1732846617420.csv',
    '1732846696465 - 1732846706002.csv',
    '1732846778730 - 1732846795963.csv',
    '1732846881373 - 1732846898112.csv',
    '1732847336599 - 1732847355797.csv'
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
