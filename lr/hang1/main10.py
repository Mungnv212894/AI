import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV
file_paths = [
    '1732592611160 - 1732592629601.csv', '1732593842367 - 1732593858712.csv',
    '1732593077266 - 1732593102117.csv', '1732594102664 - 1732594122693.csv',
    '1732593245817 - 1732593267974.csv', '1732594261305 - 1732594278793.csv',
    '1732593382925 - 1732593402435.csv', '1732594520435 - 1732594537230.csv',
    '1732593539899 - 1732593559902.csv', '1732593672177 - 1732593691817.csv'
]

# Tạo một cửa sổ đồ thị với 2 hàng, 5 cột (tổng cộng 10 đồ thị)
fig, axs = plt.subplots(2, 5, figsize=(15, 8))

# Lặp qua các file CSV và vẽ vào các subplot tương ứng
columns_to_plot = ['b', 'c', 'd', 'e', 'f']
for i, file_path in enumerate(file_paths):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

    # Chuyển vị trí subplot theo chỉ số
    row = i // 5
    col = i % 5

    # Vẽ dữ liệu vào subplot
    for col_to_plot in columns_to_plot:
        axs[row, col].plot(data['a'], data[col_to_plot], label=col_to_plot)
    
    # Thiết lập tiêu đề và các thông số
    axs[row, col].set_title(f'Plot {i+1}')
    axs[row, col].set_ylim(0, 4095)
    axs[row, col].set_xlabel('Time (a)')
    axs[row, col].set_ylabel('Values')
    axs[row, col].grid(True)
    axs[row, col].legend()

# Cải thiện khoảng cách giữa các đồ thị
plt.tight_layout()
plt.show()
