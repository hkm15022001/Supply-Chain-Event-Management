import csv
from geopy.distance import geodesic

# Cập nhật thông tin về mã zip của mỗi thành phố
locations = {
    'Hà Nội': {'coordinates': (21.0285, 105.8542), 'zip_code': '000084'},
    'Hải Phòng': {'coordinates': (20.8617, 106.6832), 'zip_code': '000083'},
    'Hải Dương': {'coordinates': (20.9403, 106.3434), 'zip_code': '000085'},
    'Quảng Ninh': {'coordinates': (21.0169, 107.2733), 'zip_code': '000086'},
    'Bắc Giang': {'coordinates': (21.2724, 106.1946), 'zip_code': '000087'},
    'Thái Nguyên': {'coordinates': (21.5947, 105.8482), 'zip_code': '000088'},
    'Lạng Sơn': {'coordinates': (21.8456, 106.7574), 'zip_code': '000089'},
    'Bắc Ninh': {'coordinates': (21.1861, 106.0632), 'zip_code': '000090'},
    'Hà Nam': {'coordinates': (20.6165, 105.9724), 'zip_code': '000091'},
    'Nam Định': {'coordinates': (20.4264, 106.1630), 'zip_code': '000092'}
}

# Tạo ma trận khoảng cách
locations_list = list(locations.keys())
num_locations = len(locations)
distance_matrix = [[0 for _ in range(num_locations)] for _ in range(num_locations)]

for i in range(num_locations):
    for j in range(num_locations):
        coords_1 = locations[locations_list[i]]['coordinates']
        coords_2 = locations[locations_list[j]]['coordinates']
        distance = geodesic(coords_1, coords_2).kilometers
        distance_matrix[i][j] = distance

# Ghi vào file CSV
with open('distance_matrix.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Ghi tiêu đề (tên thành phố và mã zip)
    header = ['', ''] + locations_list  # Thêm cột trống và cột tên thành phố để làm tiêu đề cho cột mới
    writer.writerow(header)
    
    # Ghi dữ liệu
    for i, row in enumerate(distance_matrix):
        zip_code = locations[locations_list[i]]['zip_code']
        writer.writerow([locations_list[i], f"'{zip_code}"] + row)

print("File CSV đã được tạo: 'distance_matrix.csv'")
