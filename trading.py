from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON received'}), 400

        # حدد نوع الصفقة من الكلمة المرسلة في المفتاح "text"
        order_type = data.get("text")
        entry = float(data.get("entry"))
        sl = float(data.get("sl"))
        tp1 = float(data.get("tp1"))
        tp2 = float(data.get("tp2"))
        tp3 = float(data.get("tp3"))

        logging.info(f"Received signal: {order_type}")
        logging.info(f"Entry: {entry}, SL: {sl}, TP1: {tp1}, TP2: {tp2}, TP3: {tp3}")

        # هنا يمكنك مستقبلاً تنفيذ الصفقة في MT5 أو إرسالها لتلغرام
        # ...

        return jsonify({'status': 'Signal received'}), 200

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
