import pandas as pd
import matplotlib.pyplot as plt

# Danh sách các file CSV cần vẽ
file_paths = [
    '1732705053258 - 1732705062087.csv',
    '1732705071943 - 1732705079494.csv',
    '1732705088520 - 1732705097386.csv',
    '1732705383340 - 1732705391383.csv',
    '1732705415892 - 1732705424073.csv',
    '1732705431985 - 1732705439967.csv',
    '1732705665861 - 1732705673976.csv',
    '1732705679819 - 1732705687920.csv',
    '1732705693940 - 1732705702062.csv',
    '1732705956859 - 1732705965446.csv'
]

# Tạo một cửa sổ vẽ đồ thị lớn
plt.figure(figsize=(15, 30))

# Lặp qua các file CSV
for i, file_path in enumerate(file_paths):
    data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

    # Tạo đồ thị con cho mỗi file
    plt.subplot(5, 2, i + 1)  # Tạo 5 hàng, 2 cột, vị trí thứ i+1
    columns_to_plot = ['b', 'c', 'd', 'e', 'f']
    for col in columns_to_plot:
        plt.plot(data['a'], data[col], label=col)

    # Tuỳ chỉnh giới hạn trục y và nhãn trục
    #plt.ylim(0, 2500)  # Giới hạn trục y
    plt.title(f'Plot of {file_path}', fontsize=10)
    plt.xlabel('Time (a)', fontsize=8)
    plt.ylabel('Values', fontsize=8)
    plt.grid(True)
    plt.legend()

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
