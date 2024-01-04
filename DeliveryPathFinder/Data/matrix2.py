import sqlite3
import csv
from geopy.distance import geodesic

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('E:/scem-1/Back-end/db/gorm.sqlite')
cursor = conn.cursor()

# Truy vấn dữ liệu vị trí từ cơ sở dữ liệu
cursor.execute("SELECT city, latitude, longitude FROM delivery_locations")
rows = cursor.fetchall()

# Chuyển dữ liệu từ cơ sở dữ liệu thành danh sách tuples
locations = [(row[0], (row[1], row[2])) for row in rows]

# Tạo ma trận khoảng cách
num_locations = len(locations)
distance_matrix = [[0] * num_locations for _ in range(num_locations)]

# Tính toán khoảng cách giữa các điểm và lưu vào ma trận khoảng cách
for i in range(num_locations):
    for j in range(num_locations):
        distance_matrix[i][j] = geodesic(locations[i][1], locations[j][1]).kilometers

# Đóng kết nối đến cơ sở dữ liệu
conn.close()

# Write the distance matrix to a CSV file with City names as headers and AreaCode as the second column
with open('distance_matrix1.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row with City names
    header_row = [""] + [location[0] for location in locations]
    writer.writerow(header_row)

    # Write data rows with City names and distance values
    for i, row in enumerate(distance_matrix):
        data_row = [locations[i][0]] + row
        writer.writerow(data_row)
num_rows = len(distance_matrix)  # Số hàng trong ma trận
num_columns = len(distance_matrix[0])  # Số cột trong ma trận (giả sử mọi dòng có cùng số cột)

print(f"Số hàng: {num_rows}")
print(f"Số cột: {num_columns}")
print("Distance matrix has been written to distance_matrix1.csv")
