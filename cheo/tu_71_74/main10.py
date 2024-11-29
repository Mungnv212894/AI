import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732850761365 - 1732850768543.csv',
    '1732850852244 - 1732850866507.csv',
    '1732850949893 - 1732850956937.csv',
    '1732851139187 - 1732851146346.csv',
    '1732851254026 - 1732851261302.csv',
    '1732851368819 - 1732851375545.csv',
    '1732851545076 - 1732851552909.csv',
    '1732851616621 - 1732851623150.csv',
    '1732851736928 - 1732851743414.csv',
    '1732851903360 - 1732851910860.csv'
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
