from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Example GET route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello from Flask API!"
    }
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
