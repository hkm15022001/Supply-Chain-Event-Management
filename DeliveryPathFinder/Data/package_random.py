import pandas as pd
import random

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('Packages.csv')
print(df.head())
# Định nghĩa dict locations
locations = {
    'Hanoi': {'coordinates': (21.0285, 105.8542), 'zip_code': '000084'},
    'Haiphong': {'coordinates': (20.8617, 106.6832), 'zip_code': '000083'},
    'Hai Duong': {'coordinates': (20.9403, 106.3434), 'zip_code': '000085'},
    'Quang Ninh': {'coordinates': (21.0169, 107.2733), 'zip_code': '000086'},
    'Bac Giang': {'coordinates': (21.2724, 106.1946), 'zip_code': '000087'},
    'Thai Nguyen': {'coordinates': (21.5947, 105.8482), 'zip_code': '000088'},
    'Lang Son': {'coordinates': (21.8456, 106.7574), 'zip_code': '000089'},
    'Bac Ninh': {'coordinates': (21.1861, 106.0632), 'zip_code': '000090'},
    'Ha Nam': {'coordinates': (20.6165, 105.9724), 'zip_code': '000091'},
    'Nam Dinh': {'coordinates': (20.4264, 106.1630), 'zip_code': '000092'}
}

# Hàm để chọn ngẫu nhiên một key từ locations
def get_random_location_key():
    return random.choice(list(locations.keys()))

# Thay đổi giá trị trong cột 'Address' bằng các giá trị ngẫu nhiên từ keys trong locations
df['Address'] = df['Address'].apply(lambda x: get_random_location_key())

# Lưu DataFrame đã thay đổi vào file mới (nếu cần)
df.to_csv('updated_package.csv', index=False)

# In ra 5 dòng đầu tiên để xem kết quả
print(df.head())
