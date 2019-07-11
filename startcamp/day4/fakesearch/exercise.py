'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
totalq1 = 0
averageq1 = 0
for v in score.values():
    totalq1+=v
averageq1=totalq1/len(score)
print(averageq1)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
totalq2=0
lenq2=0
for k,v in scores.items():
    lenq2 +=len(scores[k])
    for i,j in v.items():
        totalq2+=j
averageq2=totalq2/lenq2
print(averageq2)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
ansq3=[]

for i,j in city.items():
    temp=0
    for v in j:
        temp += v
        avgtemp= temp/len(j)
    ansq3.append(avgtemp)
print(ansq3)



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

highest=''
lowest=''
htemp=0
ltemp=0
for k,v in city.items():
    for t in v:
        if t>htemp:
            htemp=t
            highest=k
        if t<ltemp:
            ltemp=t
            lowest=k
print(f'가장더운 곳은 {highest} : {htemp} 도')
print(f'가장추운 곳은 {lowest} : {ltemp} 도')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?




# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
ans='아니오'
htemp3=0
ltemp3=0
for i in city['서울']:
    if i>htemp3:
        htemp3=i
    if i<ltemp3:
        ltemp3=i
if (ltemp3<2) and (htemp>2):
    ans="네"
print(ans)