
import requests
from decouple import config

base = 'https://api.telegram.org/'
token = 'bot'+config('TELEGRAM_TOKEN')
method = 'sendmessage'
chat_id = '861812746'
text = '안녕'
url = base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text
res = requests.get(url)

print(res.text)


# @app.route("/message")
# def message():
#     return render_template('home.html')

