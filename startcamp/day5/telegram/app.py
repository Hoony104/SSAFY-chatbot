from flask import Flask, render_template, request
import requests
from pprint import pprint
from decouple import config
import random
app = Flask(__name__)

token = config('TELEGRAM_TOKEN')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mresult')
def mresult():
    # base = 'https://api.telegram.org/'
    # token = 'bot'+config('TELEGRAM_TOKEN')
    # method = 'sendmessage'
    # chat_id = '861812746'
    # text = request.args.get('textmessage')
    # url = base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text


    base = 'https://api.telegram.org'

    method = 'sendmessage'

    updates=f'{base}/bot{token}/getupdates'
    status=requests.get(updates).json()
    pprint(status)
    right=status.get('result')[0].get('message').get('from').get('id')
    # chat_id = '861812746'
    text = request.args.get('textmessage')
    url=f'{base}/bot{token}/{method}?chat_id={right}&text={text}'

    res = requests.get(url)
    res

    print(status)

    return render_template('mresult.html', text=text)

@app.route(f'/{token}', methods=['POST'])
def webhook():

    res=request.get_json()
    # print(pprint(res))
    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')
    
    base='https://api.telegram.org'
    method='sendMessage'
    
    if res.get('message').get('photo') is not None:
        file_id = res.get('message').get('photo')[-1].get('file_id')
        file_res = requests.get(f'{base}/bot{token}/getfile?file_id={file_id}')
        file_path = file_res.json().get('result').get('file_path')
        file_url = f'{base}/file/bot{token}/{file_path}'

        image = requests.get(file_url, stream=True)

        url = "https://openapi.naver.com/v1/vision/celebrity"
        headers={
            "X-Naver-Client-Id" : config('NAVER_ID'),
            "X-Naver-Client-Secret" : config('NAVER_SECRET')
        }
        files={
            'image':image.raw.read()
        }

        clova_res = requests.post(url, headers=headers, files=files)
        name = clova_res.json().get('faces')[0].get('celebrity').get('value')
        percent = str(int(clova_res.json().get('faces')[0].get('celebrity').get('confidence')*100))
        text = f'{name}와 {percent}% 일치'
 
    else:
        if 'lotto' in text:
            text = str(sorted(random.sample(range(1,46),6)))
        elif text[:3] == '/번역':
                url='https://openapi.naver.com/v1/papago/n2mt'
                headers={
                    "X-Naver-Client-Id" : config('NAVER_ID'),
                    "X-Naver-Client-Secret" : config('NAVER_SECRET')
                }
                data = {
                    'source':'ko',
                    'target':'zh-CN',
                    'text':f'{text}'[3:]
                }
                res = requests.post(url, headers=headers, data=data)
                text = res.json().get('message').get('result').get('translatedText')  
        if 'love' in text:
            text = 'i like you'
    url=f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
    requests.get(url)
    return '', 200



if __name__=='__main__':
    app.run(debug=True)