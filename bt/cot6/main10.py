import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV
file_paths = [
    '1732784622311 - 1732784630848.csv',
    '1732784713768 - 1732784722863.csv',
    '1732784808880 - 1732784824859.csv',
    '1732784936685 - 1732784948610.csv',
    '1732785185477 - 1732785201867.csv',
    '1732785320621 - 1732785334066.csv',
    '1732785661155 - 1732785677096.csv',
    '1732785778585 - 1732785787173.csv',
    '1732786135469 - 1732786144369.csv',
    '1732786157488 - 1732786166874.csv'
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
