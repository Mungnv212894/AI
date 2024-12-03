import pandas as pd
import csv

# Đọc dữ liệu từ file CSV và gán tên cột
input_file = "1732843602181 - 1732843609154.csv"
output_file = "output.csv"

# Đọc file CSV vào dataframe pandas
data = pd.read_csv(input_file, header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'id'])

# Tìm và thay đổi giá trị id nếu cột 1 có giá trị là 1732843606440
data.loc[data['a'] == 1732843606440, 'id'] = 'id62'

# Ghi lại file CSV với dữ liệu đã chỉnh sửa
data.to_csv(output_file, index=False, header=False)

print(f"File CSV đã được sửa và lưu tại: {output_file}")
