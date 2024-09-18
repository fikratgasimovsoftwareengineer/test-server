from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Allow CORS only for requests from the React app URL
CORS(app, resources={r"/*": {"origins": "https://ambitious-sky-0adcaca03.5.azurestaticapps.net"}})

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
