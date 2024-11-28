import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV
file_paths = [
    '1732788009739 - 1732788024051.csv',
    '1732788364542 - 1732788380732.csv',
    '1732788465183 - 1732788473899.csv',
    '1732788546753 - 1732788556492.csv',
    '1732788635301 - 1732788651759.csv',
    '1732788737524 - 1732788753826.csv',
    '1732788855887 - 1732788866602.csv',
    '1732788941173 - 1732788955835.csv',
    '1732789056438 - 1732789071917.csv',
    '1732789172916 - 1732789188189.csv'
]

# Thiết lập kích thước cửa sổ đồ thị
plt.figure(figsize=(15, 25))

# Duyệt qua từng file để vẽ đồ thị
for i, file_path in enumerate(file_paths):
    try:
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])
        
        # Tạo đồ thị con
        plt.subplot(5, 2, i + 1)  # 5 hàng, 2 cột
        columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột cần vẽ
        for col in columns_to_plot:
            plt.plot(data['a'], data[col], label=col)  # Vẽ các cột theo trục a (thời gian)

        # Cài đặt đồ thị
        plt.ylim(0, 2500)  # Giới hạn trục Y
        plt.title(f'Plot of {file_path}', fontsize=10)
        plt.xlabel('Time (a)', fontsize=8)
        plt.ylabel('Values', fontsize=8)
        plt.grid(True)
        plt.legend(fontsize=8)
    except Exception as e:
        print(f"Lỗi khi xử lý tệp {file_path}: {e}")

# Hiển thị tất cả đồ thị
plt.tight_layout()
plt.show()
