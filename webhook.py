from flask import Flask, request
import os

app = Flask(__name__)

# For browser testing
@app.route('/', methods=['GET'])
def index():
    return "Webhook running. Waiting for alerts.", 200

# For Alertmanager alerts
@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data and 'alerts' in data:
        for alert in data['alerts']:
            if alert['labels']['alertname'] == "NginxDown":
                os.system("ansible-playbook restart_nginx.yml")
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

