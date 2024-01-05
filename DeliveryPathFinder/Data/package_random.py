import pandas as pd
import random

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('updated_package1.csv')
df1 = pd.read_csv('distance_matrix1.csv')

print(df.head())

# Lấy cột 'Region' và 'City' từ df1
regions = df1['Region']
cities = df.iloc[:, 0]

# Lấy các địa chỉ từ df1 có Region là Bắc Bộ (trừ Hà Nội)
northern_addresses = df1[(regions == 'Bắc Bộ') & (cities != 'Hà Nội')].iloc[:, 0].tolist()
# Thay đổi giá trị trong cột 'Address' bằng các giá trị ngẫu nhiên từ northern_addresses
df['Address'] = random.choices(northern_addresses, k=len(df))

# Lưu DataFrame đã thay đổi vào file mới (nếu cần)
df.to_csv('updated_package.csv', index=False)

# In ra 5 dòng đầu tiên để xem kết quả
print(df.head())
