#  2일차 웹브라우저 조작



## 정보 스크래핑



### import requests

requests.get(주소) -- http status code

requests.get(주소).text -- 페이지 소스

requests.get(주소).status_code -- http status code



## import bs4

페이지 소스에서 쉽게 가져오기 위한 모듈

`bs4.BeautifulSoup(requests.get("URL".text,"html.parser").select("검색어")`

(파이어폭스 : 요소검사 - 복사 - css선택자 )





URL을 매개로 요청/응답 주고받으며, 문서형태임



## 패키지 가져오기

### PIP 명령어

`pip install 패키지명`

`pip uninstall 패키지명`





git bash 파이썬 버전변경 path

내컴퓨터 - 고급시스템설정 - 환경변수 - 시스템변수 중 path



### OS 명령어

`os.chdir('폴더명')` : 폴더위치 변경

`os.listdir()` : 현재폴더의 파일들(리스트 형태)

`os.rename('현재파일명','바꿀파일명')`

`os.system('rm a.txt 명령어')` : 터미널 명령어 직접 입력



`mv 해당파일명 바꿀파일명` 파일명 바꾸기



내장함수 open('파일명', '뭐할건지') : 파일열기

r / w / a

`open().close()`

`with open() as 변수:` close() 생략

`변수.write('~~~')`

 `open(,, encoding='utf-8')` : 한글 인코딩 추가

`변수.read()` 

 `변수.readlines()` 리스트로 라인마다 받음





dir(변수)  쓸수 있는 함수 나옴



## GIT 저장&활용법

(로컬)

`git status` 현재 상태 확인

`git log` 로그 확인

`git add .`  모든파일 저장목록에 추가

`git commit (-m "메시지":메시지 로그 남기기)`  저장하기    ::: 빠져나가기 `esc + 콜론 + wq `

---

(리모트 서버)

`git push` : 모심기

---

`git clone 복사url주소` : 통짜 내려받기

---

`git pull origin master`  변경사항 받기?

---

되돌리기 : `git checkout ~~~~`  reset, revert 등이 있음.

숨긴파일 중 .git 지우면 날아감

---

업로드 꼬였을때?

code .

git add .

git commit -m "merge conflict"

git push

---

지옥에서 온 깃

udacity   'git' '머신러닝' 100만원?

edx cousera  'cs50' 에드윗? 네이버?



http://bit.do/ssafy21



