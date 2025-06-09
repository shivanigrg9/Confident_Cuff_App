from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Confident_Cuff']
users_collection = db['users']
contacts_collection = db['contacts']  # Collection for emergency contacts
location_collection = db['locations']  # Collection for location data
health_collection = db['health']  # Collection for health data

# Route to save user data (index.html)
@app.route('/save_user', methods=['POST'])
def save_user():
    data = request.json
    user = {
        "phone_number": data.get('phone_number'),
        "country_code": data.get('country_code')
    }
    users_collection.insert_one(user)
    return jsonify({"message": "User saved successfully!"}), 201

# Route to save emergency contacts (add-contact.html)
@app.route('/save_contacts', methods=['POST'])
def save_contacts():
    data = request.json
    contacts = data.get('contacts', [])
    if not contacts:
        return jsonify({"error": "No contacts provided"}), 400

    # Save contacts to the database
    contacts_collection.insert_many(contacts)
    return jsonify({"message": "Contacts saved successfully!"}), 201

# Route to save location data (location.html)
@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.json
    location = {
        "latitude": data.get('latitude'),
        "longitude": data.get('longitude'),
        "timestamp": data.get('timestamp')
    }
    location_collection.insert_one(location)
    return jsonify({"message": "Location saved successfully!"}), 201

# Route to save health data (health.html)
@app.route('/save_health', methods=['POST'])
def save_health():
    data = request.json
    health_data = {
        "heart_rate": data.get('heart_rate'),
        "blood_pressure": data.get('blood_pressure'),
        "oxygen_level": data.get('oxygen_level'),
        "timestamp": data.get('timestamp')
    }
    health_collection.insert_one(health_data)
    return jsonify({"message": "Health data saved successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)