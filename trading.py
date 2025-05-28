from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received data: {data}")
    # هنا تقدر تحفظ البيانات في ملف أو ترسلها لـ MT5
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run()
