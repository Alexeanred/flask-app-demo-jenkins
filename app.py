# app.py

from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

# Sample route
@app.route('/hello/<string:name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

# Start Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
