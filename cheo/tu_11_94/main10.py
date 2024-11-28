import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732790885551 - 1732790894537.csv',
    '1732791013666 - 1732791033176.csv',
    '1732791130311 - 1732791140312.csv',
    '1732791242064 - 1732791251766.csv',
    '1732791446240 - 1732791465047.csv',
    '1732791572906 - 1732791584381.csv',
    '1732791664937 - 1732791684272.csv',
    '1732791787620 - 1732791799834.csv',
    '1732791916460 - 1732791937109.csv',
    '1732792057014 - 1732792077464.csv'
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
