#### 추천

- 칸 아카데미 스쿨
- y combinator
- 버클리 cs162, software engineering --> edx   agile development using ruby on rails  :  데이비드 패터슨?
- 프로그래머스??? 개발자 채용 / 코딩테스트



# https://github.com/sspy21/   -> 강의코드





# [190710] SSAFY START CAMP 3일차 

텔레그램이 목표!? 영화추천프로그램??



## Flask

- `pip install flask`

- (bash 상에서) `flask run` : 서버구동

`cd /` : 루트 ... 가장 상위 or 근본

`cd ~` : 홈 위치로 이동

`ctrl + c` 작업 취소

- BASH 한글출력 되게 바꾸기  -- BASH 상태창 우클릭 -> 옵션 -> krko, eucKR

- http://www.naver.com:80/  http -> 80포트가 기본.   https -> 443포트가 기본



---

- `from flask import Flask, render_template` :  `import flask` 만 작성 시, `flask.` 을 앞에 붙여줘야함

`@app.route("/주소")`  : url 주소 설정 (변수 입력 필요시 < 변수 >)

`def home():`

​	`return render_template('~~~.html')`

or

​	`	return render_template('파일명.html', 변수1=파이썬변수, 변수2=파이썬변수2)`

---

- `< 변수명 >` variable routing : 파이썬의 변수를 html로 가져갈때 사용

  url 주소 설정에 입력!!! 

- 스트링, 딕셔너리, 튜플만 출력으로 가능 --> 리스트 등은 스트링으로 변환해줘야 함

## datetime

`import datetime`

`from ~ import ~` 로 하면 바로 뒤의 함수 사용가능. 

`datetime.datetime.now().year` : 현재 날짜기준 연도 추출

## html 만들기 실습 

-  `! tab`  기본 템플릿 자동완성

- css : 꾸미기 도구... awesome!!
- .py에서 받아온 변수는 `{{ 변수 }}` 로 입력



## 서버자동 업데이트

- .html 파일 : vs code 에서 extensions -> live server  추가설치

- .py 파일 :  아래 코드 맨 마지막에 넣기

  ​	`if __name__ == "__main__":`

  ​	`    app.run(debug=True)`



## 주의사항

- 파일/폴더명 디폴트 설정 값..  (app.py  `and`  templates폴더 안 html, 같은폴더안에)

- 아닐 시...  `FLASK_APP=이름 flask run`  로 실행



## JSON 데이터

#### 크롬 익스텐션 .. 제이슨 뷰어 검색하여 추가

- 키밸류 페어 포맷.    파이썬은 순수 글자로 인식. parsing 필요함.

- `request.get('주소').json()`  제이슨을 파이썬 dic로 바꿈