import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'QR Doorbell is alive!'

@app.route('/notify')
def notify():
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    
    access_token = os.environ.get('MATRIX_TOKEN')
    room_id = os.environ.get('MATRIX_ROOM_ID')

    if not bot_token or not chat_id:
        return 'Missing credentials', 500
    
    if not access_token or not room_id:
        return 'Missing Matrix credentials', 500

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": "🚪 누군가 문 앞에서 기다리고 있어요!"}
    
    
    matrix_api = f"https://matrix-client.matrix.org/_matrix/client/r0/rooms/{room_id}/send/m.room.message?access_token={access_token}"
    message = {
        "msgtype": "m.text",
        "body": "🚪 누군가 문 앞에서 기다리고 있어요!"
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            return f"Telegram Error {response.status_code}: {response.text}", 500
        
        r = requests.post(matrix_api, json=message)
        if r.status_code != 200:
            return f"Matrix Error {r.status_code}: {r.text}", 500
        
    except Exception as e:
        return f"Exception during request: {str(e)}", 500

    return '🔔 방문 요청이 접수되었습니다. 잠시만 기다려 주세요.', 200