import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV mới
file_paths = [
    '1732789405195 - 1732789416153.csv',
    '1732789505737 - 1732789515641.csv',
    '1732789785939 - 1732789796183.csv',
    '1732789881017 - 1732789891550.csv',
    '1732789964639 - 1732789975175.csv',
    '1732790082060 - 1732790091525.csv',
    '1732790172709 - 1732790182674.csv',
    '1732790280624 - 1732790290013.csv',
    'output.csv',
    '1732790452543 - 1732790461614.csv',
    
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
