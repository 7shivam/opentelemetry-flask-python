from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def send_response():
    # JSON response to send
    data = {
        'name': 'Jane',
        'age': 25,
        'email': 'jane@example.com'
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
