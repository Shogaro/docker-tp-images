from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/stats', methods=['POST'])
def calculate_stats():
    data = request.json.get('numbers', [])
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = {
        'count': len(data),
        'sum': sum(data),
        'average': sum(data) / len(data),
        'min': min(data),
        'max': max(data)
    }
    
    return jsonify(result)

@app.route('/api/stats/median', methods=['POST'])
def calculate_median():
    data = sorted(request.json.get('numbers', []))
    n = len(data)

    if n == 0:
        return jsonify({'error': 'No data provided'}), 400

    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]

    return jsonify({'median': median})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)