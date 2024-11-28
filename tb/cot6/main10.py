import pandas as pd
import matplotlib.pyplot as plt

# Danh sách file CSV mới
file_paths = [
    '1732777048117 - 1732777055911.csv',
    '1732777066334 - 1732777074669.csv',
    '1732777292398 - 1732777301112.csv',
    '1732777312974 - 1732777322578.csv',
    '1732777706945 - 1732777716300.csv',
    '1732777740540 - 1732777755498.csv',
    '1732778067685 - 1732778077062.csv',
    '1732778209451 - 1732778218164.csv',
    '1732778475619 - 1732778484505.csv',
    '1732778663789 - 1732778672582.csv'
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
