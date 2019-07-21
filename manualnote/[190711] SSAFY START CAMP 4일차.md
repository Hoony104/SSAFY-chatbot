# [190711] 4일차

- 크롬 네이버 풀기 :  시작메뉴검색 - 서비스 - 크립토그래픽서비스 - 로그온 -> 로컬시스템 계정으로 변경



## 웹페이지의 종류(2가지)

- static page : 단순 동일한 정보제공.  --> github 배포

- dynamic page : 사용자 요청에 따라 다른 페이지 : 사용자 입력값 처리 필요



## 페이크 검색엔진 만들기

`<form action='서치주소'>` 

`<input name='주소에서 쓰고 있는 약어'>` 

`<button>`

`</form>`



`<a href='연결주소'>`  하이퍼링크

`<p>` paragragh 생성

`<br>` 줄바꾸기인데... 권장 X. 나중에 복잡해지면 다 깨짐



## 랜덤직업 Faker

pip install Faker

- `from faker import Faker`
- `fake = Faker('ko_KR')`



### request : url에서 입력변수값 가져오기

`from flask import request`

`변수명=request.args.get('가져올변수명')`



## html 에서  속성 입력 후 tab 키로 자동입력 가능한것 많음



randint(최소, 최대) : `import random`



min

max

flattening .. 리스트 안의 리스트를 하나의 리스트로!



팀쏘드<<머지쏘트.  파이썬 내장함수가 가장 효율적임.

안에서 두번 돌리는건 피하라.



## DICT 사용법

dict.get('key 값')  ---  에러가 안나고 None 반환  --> 유용함

아니라면 try~ except 써야함





