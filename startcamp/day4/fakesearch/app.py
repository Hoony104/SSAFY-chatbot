from flask import Flask, render_template, request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup

fake = Faker('ko_KR')
app = Flask(__name__)
sel={}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

@app.route('/result')
def result():
    name=request.args.get('name')
    if name in sel.keys():
        job=sel[name]
    else:
        job=fake.job()
        sel.update({name:job})
    
    return render_template('result.html', job=job, name=name)

@app.route('/jjack')
def jjack():
    return render_template('jjack.html')

save={}
@app.route('/destiny')
def destiny():
    babo=request.args.get('babo')
    you=request.args.get('you')
    con=[babo,you]
    conset=set(con)
    # conset=babo+"+"+you
    if conset in save.values():
        # percent = [i for i,j in save.items() if save[i]==j]
        for i,j in save.items():
            if save[i]==j:
                percent=i        
    else:
        percent=random.choice(range(50,101))
        save.update({percent:conset})
    
    # dict in dict 사용
    # if babo in babos :
    #     if you in babos[babo] :
    #         percent=babos[babo][you]
    #     else:
    #         percent = random.randint(51,100)
    #         babos[babo][you] = percent
    # else:
    #     percent = random.randint(51,100)
    #     babos[babo] = {you:percent}

    return render_template('destiny.html', babo=babo, you=you, percent=percent)

@app.route('/admin')
def admin ():
    return render_template('admin.html', save=save,sel=sel)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/rate')
def rate():
    id=request.args.get('id')
    url=f'https://www.op.gg/summoner/userName={id}'
    urlwin='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins'
    urllose='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses'
    urlwrate='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio'

    doc=BeautifulSoup(requests.get(url).text, 'html.parser')
    win=doc.select_one(urlwin).text
    lose=doc.select_one(urllose).text
    wrate=doc.select_one(urlwrate).text

    return render_template('rate.html', win=win, lose=lose, wrate=wrate)



if __name__== '__main__':
    app.run(debug=True)