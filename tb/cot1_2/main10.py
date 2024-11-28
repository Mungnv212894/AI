import pandas as pd
import matplotlib.pyplot as plt

# Danh sách 11 file CSV
file_paths = [
    '1732768625359 - 1732768633091.csv',
    '1732768942477 - 1732768952104.csv',
    '1732769363669 - 1732769372824.csv',
    '1732769385672 - 1732769404080.csv',
    '1732769573493 - 1732769583788.csv',
    '1732769595612 - 1732769604465.csv',
    '1732769862624 - 1732769873391.csv',
    '1732769888592 - 1732769897447.csv',
    
    '1732769939892 - 1732769948369.csv',
    '1732770248224 - 1732770256644.csv'
]

# Tạo một cửa sổ lớn cho đồ thị
plt.figure(figsize=(15, 33))  # Điều chỉnh kích thước phù hợp để hiển thị 11 đồ thị

# Lặp qua từng file CSV để vẽ đồ thị
for i, file_path in enumerate(file_paths):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

    # Tạo đồ thị con cho mỗi file
    plt.subplot(6, 2, i + 1)  # 6 hàng, 2 cột (để vừa 11 đồ thị), vị trí thứ i+1
    columns_to_plot = ['b', 'c', 'd', 'e', 'f']  # Các cột cần vẽ
    for col in columns_to_plot:
        plt.plot(data['a'], data[col], label=col)

    # Tuỳ chỉnh giao diện của từng đồ thị
    plt.ylim(0, 2500)  # Giới hạn trục y
    plt.title(f'Plot of {file_path}', fontsize=10)
    plt.xlabel('Time (a)', fontsize=8)
    plt.ylabel('Values', fontsize=8)
    plt.grid(True)
    plt.legend()

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
