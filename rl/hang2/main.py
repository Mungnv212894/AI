import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV và gán tên cột
file_path = "1732699567576 - 1732699577629.csv"
data = pd.read_csv(file_path, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

# Vẽ đồ thị
plt.figure(figsize=(12, 6))

# Chỉ vẽ các cột b, c, d, e, f
columns_to_plot = ['b', 'c', 'd', 'e', 'f']
for col in columns_to_plot:
    plt.plot(data['a'], data[col], label=col)

# Tuỳ chỉnh giới hạn trục y và nhãn trục
plt.ylim(0, 2500)  # Giới hạn trên của trục y là 4095
plt.title('Plot of Columns b, c, d, e, f with Time', fontsize=16)
plt.xlabel('Time (a)', fontsize=12)
plt.ylabel('Values', fontsize=12)

# Hiển thị lưới và chú thích
plt.grid(True)
plt.legend()

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
