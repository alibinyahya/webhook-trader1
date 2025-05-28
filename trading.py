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

        # تحديد نوع الصفقة (BUY أو SELL)
        order_type = data.get("text", "").upper()

        # تحويل الأرقام إلى float وتقريبها إلى منزلتين عشريتين
        entry = round(float(data.get("entry", 0)), 2)
        sl = round(float(data.get("sl", 0)), 2)
        tp1 = round(float(data.get("tp1", 0)), 2)
        tp2 = round(float(data.get("tp2", 0)), 2)
        tp3 = round(float(data.get("tp3", 0)), 2)

        # طباعة معلومات الصفقة في Log
        logging.info(f"Signal: {order_type}")
        logging.info(f"Entry: {entry}, SL: {sl}, TP1: {tp1}, TP2: {tp2}, TP3: {tp3}")

        # لاحقًا: تنفيذ الصفقة في MT5 يتم هنا

        return jsonify({'status': 'Signal received and parsed'}), 200

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
