# 텔레그램 api 이용

from decouple import config
import requests
from pprint import pprint
from flask import Flask, render_template, request
app = Flask(__name__)


token = config('TELEGRAM_TOKEN')


##텔레그램에서 상태확인하고 메시지 다시 보내기
#먼저 아무 메시지나 하나 보내기

a = requests.get(f'https://api.telegram.org/bot{token}/getupdates').json()  ## 상태 확인하기

b = a.get('result')[0].get('message').get('from').get('id')  # 아이디 추출
c = a.get('result')[0].get('message').get('text') # 메시지 추출

d = requests.get(f'https://api.telegram.org/bot{token}/senmessage?chat_id=b&text=c')  ## 메시지 받은대로 다시 보내기

# pprint(a)
# print(b)
# print(c)



### 웹훅 걸기
#(선행) ngrok 다운받아서 넣기 / cmd 에서 `ngrok http 5000` 입력하여 실행

#인터넷 주소창에서?
#(선행)(셋업신호보내기) https://api.telegram.org/bot{token}/setWebhook?url={ngrok 에서 생성된 포워딩 접속경로}/{token}

#(후행)(종료신호보내기) https://api.telegram.org/bot{token}/deleteWebhook

route = 'https://8d45e0f3.ngrok.io'




@app.route('/')

def home():
    return render_template('home.html')


@app.route(f'/{token}', methods=['POST'])
def webhook():
    res=request.get_json()
    print(pprint(res))

    return '', 200


