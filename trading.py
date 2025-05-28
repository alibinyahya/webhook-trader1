from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

SIGNAL_FILE = "last_signal.json"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        if not data:
            return "Invalid JSON", 400

        # حفظ الإشارة في ملف JSON
        with open(SIGNAL_FILE, 'w') as f:
            json.dump(data, f, indent=2)

        print("✅ Signal received and saved.")
        return "Signal received", 200
    except Exception as e:
        print("⚠️ Error:", e)
        return "Error", 500

@app.route('/last_signal', methods=['GET'])
def get_last_signal():
    if os.path.exists(SIGNAL_FILE):
        with open(SIGNAL_FILE, 'r') as f:
            data = json.load(f)
            return jsonify(data)
    else:
        return jsonify({"message": "No signal yet"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
