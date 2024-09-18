from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Allow CORS only for requests from the React app URL
CORS(app, resources={r"/*": {"origins": "https://icy-meadow-0593dc203.5.azurestaticapps.net"}})

# Example GET route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello from Flask API!"
    }
    return jsonify(data)


@app.route('/api/data', methods=['POST'])
def post_data():
    # Get JSON data from the request
    received_data = request.json
    response_message = f"Received the data: {received_data}"
    
    # Return a response
    return jsonify({"message": response_message}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
