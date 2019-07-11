import requests
from bs4 import BeautifulSoup


url='https://www.op.gg/summoner/userName=cuzz'
urlwin='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins'
urllose='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses'
urlwrate='#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.winratio'

doc=BeautifulSoup(requests.get(url).text, 'html.parser')
win=doc.select_one(urlwin).text
lose=doc.select_one(urllose).text
wrate=doc.select_one(urlwrate).text

print(win)
print(lose)
print(wrate)