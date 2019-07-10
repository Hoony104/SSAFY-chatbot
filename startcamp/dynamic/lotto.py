# lotto api를 통해 최신 당첨번호 가져오기
import requests
import random

url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
res=requests.get(url)
dict_lotto=res.json()
winner=[]
for i in range(6):
    winner.append(dict_lotto[f'drwtNo{i+1}'])


trynum=0
winnum=0
while winnum==0:
    mylotto=sorted(random.sample(range(1,46),6))
    rank=0
    for i in range(6):
        if mylotto[i] in winner:
            rank+=1
    if rank>=3:
        # print(f'Success! {8-rank} Prize!')
        if rank!=6:
            trynum+=1
        elif rank==6:
            winnum+=1
    else:
        # print("Fail!")
        trynum+=1
print(f'{trynum}번만에 성공')



