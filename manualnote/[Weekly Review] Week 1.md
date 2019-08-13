# [Weekly Review] Week 1



## 주요 배운 내용

- 카카오톡 챗봇 (해피해킹)
- 인터넷 브라우저 제어(오픈)
- 페이크 검색엔진, 랜덤직업 생성
- 파일 읽기, 쓰기
- 웹페이지에서 특정 기능(정보) 받아오기 : 코스피, 실시간검색순위
- Flask 활용하여 간단한 웹페이지 만들기 : 짝, 롤 전적 받아오기
- 텔레그램 api 활용 : 메시지 다시보내기, 자동번역(네이버파파고api), 사진으로 연예인 일치율 확인(네이버클로바 CFR)
- 웹훅 설정하기(ngrok 활용)
- 키값 숨기기



Happy Hacking! (파이썬기반 카카오챗봇)

SLACK(메신저)

TYPORA



## JSON 데이터

#### 크롬 익스텐션 .. 제이슨 뷰어 검색하여 추가

- 키밸류 페어 포맷.    파이썬은 순수 글자로 인식. parsing 필요함.
- `request.get('주소').json()`  제이슨을 파이썬 dic로 바꿈



## Git Bash CLI 제어

`cd /` : 루트 ... 가장 상위 or 근본

`cd ~` : 홈 위치로 이동

`ctrl + c` 작업 취소

- BASH 한글출력 되게 바꾸기  -- BASH 상태창 우클릭 -> 옵션 -> krko, eucKR

`echo $PATH` : 환경변수 확인



`ls -al` : (list) 폴더 안 내용물 보기

`cd 폴더명` : (change diretory) 폴더 안으로 들어가기

`cd ..` : 상위 폴더로 돌아가기

`mkdir` : (make directory) 새로운 디렉토리 생성

`pwd` : (print working directory) 현재위치 표시

`code .` : 현재폴더 기준으로 VS 에디터 열기`touch ~` : 파일만들기

`rm ~` : 파일 지우기

`touch ~` :  파일 만들기

`exit` : 터미널 종료

`mv 해당파일명 바꿀파일명` 파일명 바꾸기

`rm -rf .git` : 깃파일 삭제 (조심!)



## GITHUB

- 깃 셋업 방법

저장 폴더로 이동

`git init`

`git add .`

`git config --global user.email 주소@gmail.com`

`git config --global user.name  'Hoony'`

`git commit -m '주석'`

`git remote add origin 깃주소`

`git push -u origin master`



- 깃 주소 바꾸기

`git remote -v`

`git remote set -url 깃주소`



- 깃 업로드

`git  add .`

`git commit - m '주석' `     :::오류 진입시, 빠져나가기는 `esc + 콜론 + wq `

`git push`



- 깃 상태확인

`git status`

`git log`



- 당겨오기

`git clone 복사url주소` : 통짜 내려받기

`git pull origin master`  변경사항 받기



`git pull`



## VS Code 초기화 및 단축키

- ctrl + shift + p --> select default shell --> git bash
- ctrl + shift + ` -->  터미널 run









## ※ 사용한 내장함수

- ### dir(함수)

   사용할수 있는 명령어 나옴



- ### open 명령어 ('파일명', '뭐할건지') : 파일열기

  - r / w / a
  - `open().close()` : 오픈하고 뒤에 닫아줘야 함
  - ``with open() as <변수>:` close() 생략하는 오픈방법
  - `<변수>.write()`   #`.writelines()`
  - `open(,, encoding='utf-8')` : 한글 인코딩 추가
  - `<변수>.read()`   #`.readlines()` 리스트로 라인마다 받음
  - `list.reverse()` list를 거꾸로 뒤집기



## ※ 사용한 외장함수 (import 함수명, install 불필요)

- ### random
  
  - `random.choice([])` : 하나 고르기

  - `random.sample([],n)` : 여러개 비복원 추출하기
  
  - `randint(최소, 최대)` : 사이에서 하나 생성
  
    
  
- ### webbrowser
  
  - `webbrowser.open('url')`
  
    - ```python
      import webbrowser
      url = 'https://search.daum.net/search?q='
      keyword = list(input().split(","))  ## keword 여러개 받아서 동시에 여러창 띄우기
      for i in keyword:
      	webbrowser.open_new_tab(url+i)
      ```



- ### pprint
  - `form pprint import pprint`
  - `pprint(제이슨 변수)` 



- ### os          

  - `os.chdir('폴더명')` : 폴더위치 변경
  - `os.listdir()` : 현재폴더의 파일들(리스트 형태)
  - `os.rename('현재파일명','바꿀파일명')`
  - `os.system('rm a.txt 명령어')` : 터미널 명령어 직접 입력
  - `os.system('touch a.txt)` : 파일 생성    (`.zfill(4)` 4자리 앞쪽은 0으로 채우기)



- ## datetime
  - `import datetime`
  - `datetime.datetime.now().year` : 현재 날짜기준 연도 추출
  - 스트링으로 받기?        @@@@@@@@@@@@@@@@@확인@@@@@@@@@@@@@@@







## ※ 사용한 외장함수 (install 필요)

- ### requests

  - `pip install requests`
  - `requests.get('url')` -- http status code
  - `requests.get('url').text`-- 페이지 소스  : 딕셔너리 집합정보 
  - `requests.get('url').status_code` -- http status code
  - `requests.get('url').json()` : 제이슨형태로 파싱  @@@@@@@@@@@@@@@@@확인@@@@@@@@
  
  

- ###  requests

  - `pip install beautifulsoup4`

  - 페이지 소스에서 쉽게 조작하기 위한 모듈

  - `bs4.BeautifulSoup(requests.get("URL".text,"html.parser").select("검색어")`

  - 검색어 자리에 (파이어폭스 : 요소검사 - 복사 - css선택자/경로) 복사하여 넣음

    (인터넷은 URL을 매개로 요청/응답 주고받으며, 문서형태임)



- ### Faker

  - `pip install Faker`
  - 랜덤 직업 생성
  - `from faker import Faker`
  - `fake = Faker('ko_KR')`



- ## Flask

  - `pip install flask`
  - (bash 상에서) `flask run` : 서버구동
  - 파일/폴더명 디폴트 설정 값..  (app.py  `and`  templates폴더 안 .html, 같은폴더)
  - 아닐 시...  `FLASK_APP=이름 flask run`  로 실행

  ```python
  from flask import Flask, render_template, request
               ## import flask 만 작성 시, flask.을 앞에 붙여줘야함
  app = Flask(__name__)
  
  @app.route("/주소"(, methods=['POST']))
         ## url 주소 內 변수 필요시 < 변수 >  --> 아래 참고1
         ##methods 입력 생략시 GET 형식
  def home():
  	return render_template('~~~.html')
      # or
  	return render_template('파일명.html', 변수1=.py변수, 변수2=.py변수2)
  	## render_template 안쓰고 바로 html 형식 입력 가능 --> 아래 참고2
      
  
  
  @@@@@@@@@@@@@@@@확인필요@@@@@@@@@@@@@@@@@@@@
  
  - `< 변수명 >` variable routing : 파이썬의 변수를 html로 가져갈때 사용
  
    url 주소 설정에 입력!!! 
  
  - 스트링, 딕셔너리, 튜플만 출력으로 가능 --> 리스트 등은 스트링으로 변환해줘야 함
  
  
  ### request : url에서 입력변수값 가져오기
  .py변수명=request.args.get('가져올 url변수')
  
  
  
  링크 html 만들기
  
  ```

  ```
  # 참고1
  @app.route("/hello/<person>")
  def hello2(person):
      return f"hello{person}"
  
  @app.route("/cube/<vari>")
  def cube(vari):
      return str(int(vari)**3)
  ```

  ```python
  #참고2
  
  @app.route("/newyear")
  def newyear():
      month = datetime.now().month
      day = datetime.now().day
      today = datetime.now()
      if month == 1 and day == 1:
          return "<h1>yeppp</h1>" + str(today)
      else:
          return "<h1>Noppp</h1>" + str(today)
  ```



### 본격 html

- tab 자동입력 활용할것.

  ```python
  ! tab # 기본 템플릿 자동완성
   # css 꾸미기 도구... awesome!!
  {{변수}}  #.py에서 받아온 변수 입력 방법
  
  <form action='/html 넘어갈 주소'>
  <input name='.py로 넘겨줄 변수명'> #즉, url 주소로 넘겨줄 입력값
  <button>버튼내용</button>
  </form>
  
  <a href='연결 url'>  # 하이퍼링크
  <p>  				# paragragh 생성
  <br> 				# 줄바꾸기인데... 권장 X. 나중에 복잡해지면 다 깨짐
  
  
  <head>
  	<title>타이틀내용(탭 부분에 표시되는 말)</title>
  </head>
  <body style='background-color:'>
  	<h1 style='color:'> 내용 </h1>
      <h2></h2>
      <h3></h3>
      <ul>  # unordered list 생성,  <ol>도 있음
      	<li>리스트1</li>
          <li>리스트2</li>
          <li>리스트3</li>
      </ul>
      <a href='url'>글자내용</a>
      <img width='숫자' height='숫자' src='url링크'> #이미지추가
      <iframe width='숫자' height='숫자' src='링크' 등등 기타내용.. tab으로 하자..></iframe>
  </body>
  ```



### 서버 자동 업데이트

- .html 파일 : vs code 에서 extensions -> live server  추가설치

- .py 파일 :  아래 코드 맨 마지막에 넣기

  ```python
  if __name__ == "__main__":
      app.run(debug=True)
  ```



## 텔레그램 api활용

`https://api.telegram.org/bot{token}/ (method)` : 텔레그램 api 리퀘스트 포멧

`/getme` : text_id와 text 추출하여 활용
 https://api.telegram.org/bot(토큰 붙여넣기)/getme

`/sendmessage` : 메시지 보내기

`/getupdates` : 최신상태 확인. 웹훅 설정시 안됌



## setWebhook

신호(메시지)가 들어오면 알려줌. 상태변화를 감지

#### ngrok

내부에서만 도는 거를 외부에 걸어놓기 위해
`ngrok` 사용!  회원가입 안하면 8시간 제한  --- 회원 가입 후 다운로드
(설치아님!) cmd 들어가서 해당위치 접속 후  `ngrok http 5000`   입력

포워딩 복사  https://81ea5582.ngrok.io   
  <---  python 로컬포스트와 같이 실행 시 해당 주소로 접속 가능

http://localhost:5000/

요청을 보내는 방식은 2가지 : GET / POST
`@app.rounte( , methods=['POST'])`  미입력시에는  GET 이 원래 디폴트인데, 이번엔 POST로 입력!
비밀번호 같이 민감한 정보 등등 노출되지 말아야 할때는 GET이 아니라 POST를 씀!



`return '', 200`   --> 잘 들어오고 있어요~
웹훅을 쓰면, getupdates는 더 이상 못씀! (공식 메뉴얼 문서 참고)

시작할때 셋 웹훅 신호를 보내야함
`https://api.telegram.org/bot{token}/setWebhook?url={ngrok 에서 생성된 접속경로}/{token}`

종료할때 딜리트웹훅 신호 보내야함
`https://api.telegram.org/bot{token}/deleteWebhook`

<주의> if 나 for는 블록스코프가 아니라서 변수명 조심해야함. 전역변수처럼 됌

사진이나 파일은 텍스트 보낼 때는 포멧이 다르니, url 설정 잘 해줘야함.



- ## python-decouple(키 숨기기)

키 숨기기?  os단계에서 환경변수로?


- `pip install python-decouple`

  - 철자 주의할 것. 복붙 권장

  - .env 파일 생성후 대문자로 저장  `TELEGRAM_TOKEN='키값'`

```python
from decouple import config

config('TELEGRAM_TOKEN')
```



- `.gitignore`  최상단 폴더에 생성(.git 있는 폴더..  `ls -al` 로 확인가능)

- 숨길 파일명 입력(.env) 후 저장



#### 기타 참고

`dict.get('key값')`    or  `try ~ except`

http://www.naver.com:80/  http -> 80포트가 기본.   https -> 443포트가 기본

flattening .. 리스트 안의 리스트를 하나의 리스트로!







## 재정리

flask 에서 url에 변수 입력 받을시,

```python
@app.route("/Hi/<name>")
def Hi(name):
    return render_template('hello.html', name=name)
```

.html 페이지에서 받아온 변수는 request.args.get('변수명') 으로 정의해야 사용가능.