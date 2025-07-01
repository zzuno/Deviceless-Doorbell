import os
import requests
from flask import Flask
from dotenv import load_dotenv

# .env 로드
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return 'QR Doorbell is alive!'

@app.route('/notify')
def notify():
    # 알림용 토큰
    bot_token     = os.environ.get('BOT_TOKEN')
    chat_id       = os.environ.get('CHAT_ID')
  
    contact_name  = os.environ.get('CONTACT_NAME', '연락처')
    contact_phone = os.environ.get('CONTACT_PHONE', '010-0000-0000')

    # 필수 정보 체크
    if not bot_token or not chat_id:
        return 'Missing credentials', 500
    # Telegram 메시지 전송
    tg_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    tg_data = {"chat_id": chat_id, "text": "🚪 누군가 문 앞에서 기다리고 있어요!"}

    try:
        r1 = requests.post(tg_url, data=tg_data)
        if r1.status_code != 200:
            return f"Telegram Error {r1.status_code}: {r1.text}", 500

    except Exception as e:
        return f"Exception during request: {e}", 500

    # 사용자에게 보여줄 HTML (contact_name, contact_phone 사용)
    html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>방문 요청 접수</title>
      <style>
        body {{
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
          text-align: center;
          padding: 2rem;
          background-color: #f9f9f9;
        }}
        h1 {{
          font-size: 2.5rem;
          margin-bottom: 1.5rem;
          color: #333;
        }}
        p {{
          font-size: 1.2rem;
          line-height: 1.6;
          color: #555;
          margin: 1rem 0;
        }}
        .contact {{
          font-weight: bold;
          font-size: 1.3rem;
          margin-top: 1.5rem;
        }}
        a.call-button {{
          display: inline-block;
          margin-top: 1rem;
          padding: 0.6rem 1.2rem;
          background-color: #007BFF;
          color: #fff;
          text-decoration: none;
          border-radius: 0.3rem;
          font-size: 1rem;
        }}
        a.call-button:hover {{
          background-color: #0056b3;
        }}
      </style>
    </head>
    <body>
      <h1>🔔 방문 요청이 접수되었습니다.</h1>
      <p>혹시 저희가 부재 중이라면<br>아래 연락처로 연락을 남겨주시면 빠르게 도움드리겠습니다.</p>
      <p class="contact">{contact_name}: <a href="tel:{contact_phone.replace('-', '')}">{contact_phone}</a></p>
      <a class="call-button" href="sms:{clean_phone}">문자 보내기</a>
    </body>
    </html>
    """
    return html, 200