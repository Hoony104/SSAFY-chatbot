# [190711] SSAFY START CAMP 5일차

## 텔레그램

@botfather 추가 

`/newbot`  봇이름, 봇유저네임,  (토큰 간직할것, 키 같은거)

이모티콘도 만들수 있고... 



https://core.telegram.org/bots/api  메뉴얼 주소 (인증관련)



### getme

getme : https://api.telegram.org/bot(토큰 붙여넣기)/getme

chat_id 와 text 중요함



806226011:AAHGOE57OaHTQXwKcdolMOdUSg4irAzVLXw

861812746 - 내아이디?

806226011:봇아이디?





제이슨 변환한거 예쁘게 보기 `import pprint`  





[https://api.telegram.org/bot806226011:AAHGOE57OaHTQXwKcdolMOdUSg4irAzVLXw/sendmessage?chat_id=861812746&text=%E4%BD%A0%E5%A5%BD](https://api.telegram.org/bot806226011:AAHGOE57OaHTQXwKcdolMOdUSg4irAzVLXw/sendmessage?chat_id=861812746&text=你好)

URL로 메시지 보내기 가능 --> 파이썬으로 구현



/sendmessage

`?`  : 파라미터





메쏘드  getme getupdates sendmessage(파라미터 필요)



url 보내기 : `import requests` 후 `requests.get('url')` 

requests 는 response를 받게됨.  print하면 response 200/    .text로 출력하면  딕셔너리집합에 정보 리턴



## 키 숨기기

키 숨기기?  os단계에서 환경변수로?

echo $PATH



파이썬 decouple 설치.   복붙추천.. 하이에나 많음!!!!

```
pip install python-decouple
```



리눅스기반...    .으로 시작하면 숨김파일

`.env` 파일 생성

전역변수나 환경변수는 대문자가 관례

TELEGRAM_TOKEN='키값'



`from decouple import config`

`config('TELEGRAM_TOKEN')` 로 사용.



토큰파일 git 업로드 방지하기

`.gitignore` 최상단에 생성(.git 있는 폴더..  `ls -al` 로 확인가능)

파일명 입력(.env) 후 저장

- (주의) git 폴더 안에 다시 git폴더 만들면 힘들어짐...    (동등레벨로 관리 추천... or .git 지우기)





### setWebhook



웹훅(reverse API)  --> 신호(메시지)가 들어오면 알려주는거?  상태변화 감지

`setWebhook`  in telegram API

현재 내부(로컬호스트)에서만 도는 거를 외부에 걸어놔야함.

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







---

telegram에 request 하는 포멧.

`https://api.telegram.org/bot{token}/ (method)`

---

시작할때 셋 웹훅 신호를 보내야함

`포멧 + /  setWebhook?url={ngrok 에서 생성된 접속경로}/{token}`

종료할때 딜리트웹훅 신호 보내야함

`포멧 + / deleteWebhook`

##### (토큰의 값은 임의의 값이어도 됌...?? 모르겠다..)



<<if 나 for는 블록스코프가 아니라서 변수명 조심해야함>>



특정단어 시, 특정 출력 -- 챗봇



## 자동번역

네이버 open api 등록

아이디, 비밀번호 알아서 .env 저장.



.json()

_json()   바로 json 으로 변환하는 명령어



텔레그램  텍스트/사진/파일별로 포멧이 다름