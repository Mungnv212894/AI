import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV
file_paths = [
    '1732786487037 - 1732786496581.csv',
    '1732786705506 - 1732786714853.csv',
    '1732786983975 - 1732786993522.csv',
    '1732787086209 - 1732787095590.csv',
    '1732787242789 - 1732787250867.csv',
    '1732787352135 - 1732787366728.csv',
    '1732787549355 - 1732787558750.csv',
    '1732787656157 - 1732787671264.csv',
    '1732787768117 - 1732787782768.csv',
    '1732788134195 - 1732788149680.csv'
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
