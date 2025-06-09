from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

# ...existing routes...

@app.route('/trigger-sos', methods=['POST'])
def trigger_sos():
    try:
        subprocess.Popen(['python', 'sos/sos_alert.py'])
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500