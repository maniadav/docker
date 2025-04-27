from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data to return
dummy_data = {
    "status": "success",
    "message": "Welcome to the Flask Backend API!",
    "data": {
        "id": 1,
        "name": "Sample Item",
        "description": "This is just a dummy item for testing."
    }
}

@app.route('/')
def home():
    return "Hello, Flask API!"

@app.route('/api/dummy', methods=['GET'])
def get_dummy_data():
    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
