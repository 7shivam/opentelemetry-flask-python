from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def receive_response():
    # Send a request to Service B
    response = requests.get('http://localhost:5001/data')
    
    # Get the JSON response from Service B
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
