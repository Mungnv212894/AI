import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732780665890 - 1732780682199.csv',
    '1732780870991 - 1732780879569.csv',
    '1732781120159 - 1732781130428.csv',
    '1732783123250 - 1732783134030.csv',
    '1732781522807 - 1732781543870.csv',
    '1732781992302 - 1732782003296.csv',
    '1732782294524 - 1732782305918.csv',
    '1732782468451 - 1732782480679.csv',
    '1732782569599 - 1732782580440.csv',
    '1732782676055 - 1732782686883.csv'
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
