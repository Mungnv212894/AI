import pandas as pd
import matplotlib.pyplot as plt

# Danh sách file CSV mới
file_paths = [
    '1732779128531 - 1732779144577.csv',
    '1732779244933 - 1732779259798.csv',
    '1732779343531 - 1732779358977.csv',
    '1732779490443 - 1732779507361.csv',
    '1732779876494 - 1732779884738.csv',
    '1732780037270 - 1732780046337.csv',
    '1732780115653 - 1732780129573.csv',
    '1732780254756 - 1732780263794.csv',
    '1732780362568 - 1732780373636.csv',
    '1732780443931 - 1732780453314.csv'
]

# Kích thước cửa sổ đồ thị
plt.figure(figsize=(15, 28))

# Lặp qua từng file CSV
for i, file_path in enumerate(file_paths):
    try:
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])
        
        # Kiểm tra nếu file rỗng
        if data.empty:
            print(f"File {file_path} is empty. Skipping...")
            continue

        # Tạo đồ thị con
        plt.subplot(5, 2, i + 1)  # 5 hàng, 2 cột
        columns_to_plot = ['b', 'c', 'd', 'e', 'f']
        
        # Vẽ từng cột
        for col in columns_to_plot:
            if col in data:
                plt.plot(data['a'], data[col], label=col)

        # Cài đặt hiển thị đồ thị
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
