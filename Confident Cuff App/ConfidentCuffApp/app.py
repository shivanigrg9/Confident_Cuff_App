from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Load existing data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open(DATA_FILE, 'w') as f:
        json.dump(existing, f, indent=2)

    return jsonify({'message': 'Data saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)