# [190708] SSAFY START CAMP



## Happy Hacking! (파이썬기반 카카오챗봇)



## SLACK(메신저)



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



## TYPORA

- md 파일 작성

- 블렛 포인트 : - 기호

- 코드 정리는 : ``` 기호



## CLI(GIT BASH)

- 자동완성은  Tab 키
- `ls -al` : (list) 폴더 안 내용물 보기
- `cd 폴더명` : (change diretory) 폴더 안으로 들어가기
- `cd ..` : 상위 폴더로 돌아가기
- `mkdir` : (make directory) 새로운 디렉토리 생성
- `pwd` : (print working directory) 현재위치 표시
- `code .` : 현재폴더 기준으로 VS 에디터 열기
- `touch ~` : 파일만들기
- `rm ~` : 파일 지우기
- `touch ~` :  파일 만들기
- `exit` : 터미널 종료
- `mv 해당파일명 바꿀파일명` 파일명 바꾸기



## VS Code 초기화 및 단축키

- ctrl + shift + p --> select default shell --> git bash
- ctrl + shift + ` -->  터미널 run





## 외장함수

- random
  - random.choice([])
  - random.sample([],n)

- webbrowser
  - webbrowser.open("주소")



### 인터넷 창 켜기

---

`import webbrowser`

`url = 'https://search.daum.net/search?q='`

`keyword = list(input().split(","))`

`print(keyword)`

`for i in keyword:`

`    webbrowser.open_new_tab(url+i)`


