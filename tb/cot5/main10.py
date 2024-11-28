import pandas as pd
import matplotlib.pyplot as plt

# Danh sách file CSV mới
file_paths = [
    '1732775250434 - 1732775265463.csv',
    '1732776916251 - 1732776924929.csv',
    '1732775311818 - 1732775320479.csv',
    '1732775787916 - 1732775796209.csv',
    '1732775820995 - 1732775829472.csv',
    '1732776311659 - 1732776325929.csv',
    '1732776433598 - 1732776447328.csv',
    '1732776541543 - 1732776554278.csv',
    '1732776644599 - 1732776653950.csv',
    '1732776664399 - 1732776672380.csv'
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
