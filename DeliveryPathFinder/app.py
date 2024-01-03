from flask import Flask, request, jsonify

app = Flask("Vehicle Routing Problem")

# Route xử lý yêu cầu GET
@app.route('/api/process', methods=['GET'])
def get_data():
    # Xử lý logic ở đây, ví dụ trả về một dictionary
    data = {'message': 'Dữ liệu từ yêu cầu GET'}
    return jsonify(data)

# Route xử lý yêu cầu POST
@app.route('/api/process', methods=['POST'])
def post_data():
    # Lấy dữ liệu từ body của yêu cầu POST
    request_data = request.get_json()

    # Xử lý logic ở đây với dữ liệu nhận được từ POST request
    received_data = request_data.get('data', None)
    if received_data is not None:
        # Thực hiện các thao tác xử lý dữ liệu, ví dụ: lưu vào database, xử lý, v.v.
        result = {'message': 'Dữ liệu đã nhận được từ yêu cầu POST', 'received_data': received_data}
        return jsonify(result)
    else:
        return jsonify({'error': 'Không có dữ liệu được gửi'})

if __name__ == '__main__':
    app.run(debug=True)