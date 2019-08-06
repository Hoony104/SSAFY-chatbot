지난번껀데... vscode 라이브서버 설치

카카오 컨퍼런스? - 추첨탈락

책추천 - 정리하는 뇌

인공지능의 서비스화? 부분적으로만.. 활용 API?



트렐로? 가입   af -- 가벼운 to do 리스트 정리?  /// 지라도 있음

노션 -- 무거운내용

크롬- 모멘텀 (익스텐션) : 이쁜 바탕화면?  /// 애드블록

크롬-웹디벨로퍼(익스텐션) --- html 구조 파악

깃헙페이지로 스태틱페이지부터 만들기.

css 뽀개면 페이지 망가짐. : 웹 디벨로퍼(크롬 익스텐션)

프리코드캠프 추천!



## 자리이동(git 흔적 정리)

```
git credential reject
protocol=https
host=github.com
```

```
git credential reject
protocol=https
host=lab.ssafy.com
```

```
git config --list # 확인
git config --global user.name '본인'
git config --global user.email '본인꺼'
```



lorem pixel : 랜덤이미지

lorem ipsum : 더미 텍스트?

색상 https://htmlcolorcodes.com/

https://startbootstrap.com/  공짜 부트스트랩



## 가상환경 설정

```
1.가상환경설치폴더 생성
`mkdir ~/python-virtualenv`
2.가상환경설치
`python -m venv ~/python-virtualenv/3.7.3`
3.실행시킬 폴더로 이동 후 가상실행
`source ~/python-virtualenv/3.7.3/scripts/activate`
4.사용종료후 끄기
`deactivate`
(5)약어 지정. 
.bashrc
alias venv='source ~/python-virtualenv/3.7.3/scripts/activate' 
리로드 `source ~/.bashrc`
```









# [Weekly Review] Week4~5

### 사용법

주석 <!-- 내용 -->  컨트롤 슬래시



2스페이스 고치기

. vscode - 컨트롤쉬프트p  -- preference: open settings(JSON)-- 두번째 제이슨꺼(디폴트 말고) -- 아래 추가

```
"[html]":{
        "editor.tabSize": 2
    },
    "[css]":{
        "editor.tabSize": 2
    }
```

or beautify  설치. /// 쉬프트 알트 f 

//강제설정  indent using space -->2  



# HTML

### 기초구조

html을 볼때는 트리의 노드, 계층구조를 생각할것.

- 문서타입 선언부

- html요소

  ```
  <html lang='ko'>  lang 부분은 없어도 되는데, 웹 접근성을 위해 입력(스크린 리더 등,,) 디폴트는 en
  ```

- 헤드부

  ```
  문서제목, 인코딩(문자코드) 외 여러정보. 브라우저에 나타나지 않음
  og 오픈그래프 , 요약정보
  메신저 메시지 미리보기 등의 기능도 헤드 이용 / 메시지로 링크보낼때 나타나는 작은 그림도 헤드에 있음
  ```

- 바디부

  표시될 메인 내용

  

## 작성 관례

```
엘레먼트:소문자 , 속성(어트리뷰트): 더블코트 `src=" "` ,
속성="값"  붙여쓰기, 상하위 관계에서는 2space가 관례
```



## TAG와 DOM TREE

자바스크립트의 ~~ 와 같음.

### 주석

`<!-- 주석내용 -->`

### Element(요소)

태그와 내용으로 구성 `<h1>내용</h1>`

셀프클로징 되는 요소 : `<imag   />`

태그의 속성과 속성값이 존재

### DOM 트리

부모(parent)-자식(child)관계  /  형제(sibling)관계

### Semantic Tag

- non semantic : div(단순공간분할) , span

- semantic(의미론) tag: html5에서 새로 지정됨.

  ```
  (header, nav, aside, section, article, footer)
  
  header : 페이지 상단의 헤더
  nav : 내비게이션
  aside : 사이드에 위치, 메인과 관련석이 적은 컨텐츠
  section : 컨텐츠 그룹
  article : 문서 안에서 독립적으로 구분되는 영역
  footer : 푸터.. 페이지나 컨텐츠 하단?
  
  ★웹디벨로퍼(크롬의 익스텐션) -- 인포메이션 - 다큐먼트아웃라인 에서 페이지구조 확인가능
  ```

### SEO(search engine optimization, 검색엔진 최적화)

```
태그를 잘 정리하는 것이 검색에 굉장히 중요함 검색에 잘 걸리게끔.
검색엔진의 크롤러가 잘 분류하게끔... 타이틀내용이 뜸.
```



## 실습내용 정리(다시 정리 필요)

#### emmet doc 참고

ol>li*4` + tab! /// 응용 가능함    

취소선,, `<strike></strike>`    `<s></s>`   `<del></del>`

굵게...  `<b></b>`  `<strong></strong>`

이탤릭 `<i></i>`

`<p></p>`  문단 공간 생성... 줄바꿈 포함 || 블락베이스 .      cf>  `<a>이건 한줄 다 안먹음</a>`

가로줄긋기 `<hr></hr>`



MDN web docs  --- : 교과서급?   html css javascript 등

href="주소"



id할당 : 속성부여하거나 해당위치로 이동

<img> 의 alt 속성 : 이미지 표시 못할때 출력할 내용  (시각장애인 안내용도로도 쓰임)

table : 게시판  tr  td      th는 헤더로 강조

form 으로 감싸는 이유 ---  action으로 내용을 통째로 전송하기 위해.

placdholder - 클릭하는순간 사라짐

value - 클릭해도 남아있음.

`<p></p>` 입력시 약간의 줄간격이 생김

`<span></span>` 그냥 글쓰고싶을때?



보통 속성 value는 숫자등으로 간단히 표기하고, 서버에서 진짜 내용을 처리하게끔 함.(데이터 패킷 줄이기)



구글폰트   Noto sans KR  //  산세리프체:글자에 꺾임?이 없는 모양



절대경로/상대경로 

절대경로 : 루트폴더(내 컴퓨터 - C드라이브) 부터 찾는것

상대경로 : 워킹디렉토리 기준.. html에서는 상대경로를 주로 씀.



## CSS

스타일을 주는 3가지 방법 : 인라인, 임베디드,외부참조

`.class` / `#id`
다중 조건 설정 시, 가까운 거부터 적용됌 -- 인라인보다 강한 ! 도 있음..

```
<!--인라인-->
<h1 style="속성:값;속성:값;">내용</h1>
```

```
<!--임베디드-->
<style>
  h1{
  color:blue;
  font-size:15px;
  }
</style>
```

```
<!--링크-->
<link rel="stylesheet" href="링크">


```



html은 데이터를 줄이고자, 공백조차 없앨수 있음 -- 어글리파이어, 뷰티파이어



css 참고

https://developer.microsoft.com/en-us/microsoft-edge/platform/usage/



#### 크기 설정

```
웹에서의 픽셀은 상대적. 사용 기기에 따라 달라짐. 브라우저는 약간 절대화(1/96inch)

px : 디바이스별로 픽셀 크기 다름..  브라우저 1px=1/96inch
% : 요소 지정 사이즈에서 상대적인 비율
em : 상대배수단위, 1em=100%
rem(root em) : 최상위요소 html 기준 em단위
viewport : IE 완전히 지원하지 않음,  디바이스별 크기를 보완하기 위함
	vw(너비의 1/100) vh(높이의 1/100)
    vmin(작은쪽의 1/100) vmax(큰쪽의 1/100)
```



#### Box model

네모난 모양의 마진/보더/패딩/컨텐츠 로 구성

`<p></p>` 인접한 p끼리는 마진 공유 (16)  마진콜렙싱!  --> 싫으면 `<div>`

#### display

````
block : 화면 가로 전체 차지. inline요소 포함 가능
		너비/좌우마진auto 조정을 통해 가운데 정렬 가능
		div,h1~6, p, ol, ul, li, hr, table, form 등등
inline : 기존 라인에서 시작. 컨텐츠 너비만큼만 차지.
		width,height, margin-top/bottom 지정불가.
         상하여백은 line-height로 지정
         span,a,img,br,input,button,select,form내부요소 등
inline-block : inline처럼 표시되면서, width등의 속성 지정 가능
none : 요소를 표시하지 않음.(공간도 사라짐)
하나더...
````

#### visibility 

```
visible
hidden : 안보이게 함(공간은 유지) <<!--display:none 과 차이-->>
```



#### background-image

```
style="background-image: url('주소')"
opacity(투명도) 설정으로 배경화면으로 만들수 있음
```

#### Font&Text

````
font-size : 글자크기
font-family : 글꼴
letter-spacing : 자간
text-align : 정렬
white-space : 여백설정... normal/norwrap,pre,pre-wrap,pre-line 등
````

### Position

```
static : 기본값. 부모가 있으면 부모기준으로 배치
relative: 원래 자기가 들어갈 위치 기준 이동, 기존자리는 차지.
absolute : 스태틱(아무것도 지정되지 않은것) 이 아닌, 프로퍼티가 선언된 상위객체의 위치 기준으로 이동. 상하 or 좌우 선언되지 않으면 자기위치 기준으로 이동.(거리 0이라도 선언되면 이동함)
fixed : 뷰포트기준,  스크롤 되어도 사라지지 않음.

겹친거 조절하는 z-index도 있음.  미설정시 0, 높은게 앞으로 나옴
```



## Bootstrap

https://getbootstrap.com/ 

부트스트랩 - CDN 사용하기 // body 맨 아래에 붙여야 성능상 더 좋음

```
CDN(content delivery network)을 복사해서 쓰자..(starter template)
여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
여러가지 이점 : end-user와 가깝기에 속도가 빠르고, 서버에서 내주는게 아니라서 서버 부하 경감, 적절한 캐쉬설정으로 빠름.
```

디자인의 추세.... 스마트폰의 등장으로 인한 디자인의 통일화

이를 도와주는 대표적인 프레임워크 : 부트스트랩 / 머터리얼(디자인)라이즈 

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
```

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
```



#### 본격 꾸미기

id/class/형제관계도 탭으로 emmet 가능 `#ssafy` `.ssafy`  `p+h2`

인라인(span 등)은 소속된 곳의 css 같이 먹게 됌... 따로 지정가능.

```
# css 에서 특정 부분만 지정 가능(`>`트리구조, `:`상세지정)
ol>li {
  color:whitesmoke;
}
ol>li:nth-child(6){
  color:red;
}
```

```
p:nth-of-type(2) #p 중에서 두번째
p:nth-child(2) # 두번째가 p이면 적용
```

```
\`*` 모든걸 지정
a+ul{}  다음에 오는거 하나만 (잘안씀)
a~ul{} 뒤에 오는것 모두 (잘안씀)
```



a태그 새탭에서 오픈하는 속성 : `target="_blank"`



### 속성셀렉터

특정 속성을 갖고 있거나, 특정 속성의 특정 어트리뷰트를 갖는 태그만 선택.

```a[속성]
h1[title]   or   h1[title="this"]
```



#### ☆요소중앙정렬

```
수평
1.인라인 : 부모요소에 text-align:center 넣기
2.블락 : 한개짜리 - width 설정후 margin: 0 auto
         두개이상 - 부모에 text-align:center
                   자식에 display:inline-block  
          ※인라인 블락 설정 시, width나 max-width 설정해줘야 함.
          ※세로로는 height, vertical-align:top 같은거 줘야함.
수직
1.인라인 : 한줄이면 - display:block 후, height와 line-height를 같게
					※white-space :nowrap 으로 자동줄바꿈 방지
	      여러줄 - 부모에 display:table
	              자식에 display:table-cell, vertical-align:middle
2.블락 : 높이 알때 - 부모에 position:relative
                    자식에 position:absolute 후 height 설정,
                  top:50%, margin-top을 height의 절반만큼 마이너스
 높이 모를때 - 높이알때에 magin-top 대신 transform:translateY(-50%)
동시
1.크기 알때 - 부모에 position:relative;
             자식에 position:absolute top:50% left:50%
                (1)위와 왼쪽에 각각 50%씩 마진 마이너스로 주기
                (2)transform: translate(-50%,-50%)
```



 ### CSS reset

부트스트랩은 CSS의 기본 설정을 customize 해놨음(reboot, 다운로드 받으면 확인 가능)

1.1스페이싱(마진조정)  `m-5` 

```
!important  상속순서 무시.. 최우선
.mx .py : 마진과 패딩 조절.   브라우저에서 기준! 1rem=16px
mt-2 = 8px // mt-3 (기준!!) = 16px  // mt-4 = 24px  // mt-5 = 48px
mt-n2/auto : negative나 auto로 줄수도 있음

기존 ... 블락 요소(1. 부모에 텍스트 얼라인 센터, //  너비 준 다음에, 마진 좌우 각각 오토)

text-center : 가운데정렬
```

1.2 컬러

```
#부트스트랩 기본컬러
primary #007bff
secondary #6c757d
success #28a745
info #17a2b8
warning #ffc107
danger #dc3545
light #f8f9fa
dark #343a40
```

```
.bg-★color★
.text-★color★
alert alert-★color★
btn btn-★color★   : a태그도 가능
.navbar-★color★(글자색) .bg-★color★(배경색)
```

1.3 보더

```
.border border-secondary
.rounded-circle : 진짜 원
.rounded-pill : 알약모양.. 테두리만
```

1.4 디스플레이

```
.d-block
.d-inline
.d-none  : 공간조차 안보이기  .d-hidden : 공간은 유지하고 안보이기

반응형
.d-sm-none     xs(디폴트)/sm/md/lg/xl ///  스마트폰/태블릿/컴퓨터?
       breakpoint.  기기 크기 기준.... 그리드 배울때 다시 할거임
.col-sm-none

```

1.5포지션

```
.position-static	-relative 	-fixed 	-absolute
.fixed-top   -bottom
```

1.6 텍스트

```
.text-center  	-right 	-left
.font-weight-bold 	-italic
```

기타 Components들은 공식문서에 들어가서 확인.



## 그리드

```
보통 12칼럼기준으로 많이 사용함.
1. 컨테이너 선언.   가로기준으로 쌓아올리는 느낌.
   보통 호환성을 위해 1080px(~1100px 이하) 기준으로 함.
   `.container-fluid`  >>  끝까지 넓게 쓸때
2. 행 선언.
   `.row`  `display:flex` 가 내포되어 있음.
3. 열 선언.
   col-그리드칸수   :   마진이 아니라 패딩으로 간격조절해야함
```

```
반응형 -- 그리드를 풀어서 기기 크기에 맞게 세로로 쌓게끔 만들기
xs/sm/md/lg/xl
col-sm-4  (작아져서 sm이 되는순간 그리드 해제)   동시에 두개 이상씩 조건 넣으면 완성
```









