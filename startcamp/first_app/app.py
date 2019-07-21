from flask import Flask
import random
import requests
import bs4
from datetime import datetime
app = Flask(__name__)

#1. 주문 받는 방식(어떻게)
@app.route("/")
#2. 무엇을 제공할지(무엇)
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "hi earth!"

# 1. /name
@app.route("/name")
def name():
    return "KMH"
# 2. 영문이름

@app.route("/hello/<person>")
def hello2(person):
    return f"hello{person}"

@app.route("/cube/<vari>")
def cube(vari):
    return str(int(vari)**3)

@app.route("/lotto")
def lotto():
    r=sorted(random.sample(range(1,46),6))
    R=''
    # J=''
    for item in r:
        R+=str(item)
        R+=','
    # for item in r:
    #     J+=str(item)
    # J=','.join(J)
    return str(R[:-1])
    # return J

    ##str(sorted(~~~~))


@app.route("/menu")
def menu():
    mlist=['사천식해물잡탕밥','순두부찌개']
    rmenu=random.choice(mlist)
    return rmenu

    ##str(random.choice(~~~~))

@app.route("/kospi")
def kospi():
    url="https://finance.naver.com/sise/"
    page=requests.get(url).text
    docu=bs4.BeautifulSoup(page,'html.parser')
    kospi=docu.select_one('#KOSPI_now').text  
    return kospi

@app.route("/newyear")
def newyear():
    month = datetime.now().month
    day = datetime.now().day
    today = datetime.now()
    if month == 1 and day == 1:
        return "<h1>yeppp</h1>" + str(today)
    else:
        return "<h1>Noppp</h1>" + str(today)

# /index
@app.route('/index')
def index():
    return '<html><head><body><h1>홈페이지</h1><p>이건 내용</p></body></head></html>'