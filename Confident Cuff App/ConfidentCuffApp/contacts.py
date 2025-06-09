from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Path to the JSON file where contacts will be saved
CONTACTS_FILE = 'emergency_contacts.json'

@app.route('/')
def index():
    return render_template('add_emergency_contacts.html')

@app.route('/save_contacts', methods=['POST'])
def save_contacts():
    # Get the form data
    contact1 = request.form['contact1']
    contact2 = request.form['contact2']

    # Create a dictionary with the contacts
    contacts = {
        'contact1': contact1,
        'contact2': contact2
    }

    # Save the contacts to a JSON file
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

    # Optionally, redirect back to the form or show a success message
    return "Contacts saved successfully! <a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)