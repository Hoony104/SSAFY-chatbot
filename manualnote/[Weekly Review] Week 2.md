# [Weekly Review] Week 2



# DAY 1

## BASH 명령어

`python -i` : idle 터미널 실행하기

`exit()` : idle 터미널 종료



git 폴더 바꾸기

`git clone '복사한 주소 or repository 이름' '바꿀이름'`



## JUPYTER NOTEBOOK (install 필요)

`pip install jupyter`

MD 작성가능 / IDLE 형태로 활용가능



## 실행코드 약어 지정하기

`jupyter notebook` : 실행코드

```c
cd ~ : 홈(상위)폴더로 이동
code .bashrc : 약어 파일 만들기 
	VS code 에서 열리면 
	alias jn='jupyter notebook'   입력 후 저장 닫기
터미널 재실행 후
source ~/.bashrc
```



## 파이썬 기초

#### 식별자

 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름. 첫글자에 숫자X

```python
#예약어 확인
import keyword
print(keyword.kwlist)

False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

#### 내장함수

`str, print` 등... 사용자가 함수 내용 변경 가능함 --> 주의할것

변경한거 삭제하려면..

1. --- Kernel --- restart&clearoutput
2. `del str`



#### 인코딩 선언

```python
# -*- coding: <encoding-name> -*- 
주석이 아니라 python parser에 의해 읽혀짐. 선언하지 않아도 utf-8로 디폴트 되어있음
```



#### 주석

 #(single line) or '''(multi line)

`함수.__doc__` : 해당 함수의 주석을 볼수 있음. 함수 정의 바로 아래에 docstring을 쓰면 함수주석 속성 부여.



#### 코드라인

한줄에 여러개 쓸땐 `; ` 삽입

스트링 멀티라인 `\` (줄바꿈 기능) 로도 입력가능  -- (\n 과 다름)



## 수치형

#### 정수(int)

- arbitrary-precision arithmetic : 메모리 유동관리. 아주 큰 정수 표현 시 오버플로우가 없음

```python
import sys
a=sys.maxsize  # 시스템에서 표현 가능한 최대 정수(32bit? 64bit?)
```



#### 부동소수점(float)

- floating point rounding error 발생 : 실수 처리할때 조심해야함

  ```python
  ##처리방법
  1. abs(a-b) <= 1e-10
  2. import sys
     abs (a-b)  <= sys.float_info.epsilon
  3. import math
     math.isclose(a,b)
  ```



#### 복소수(complex)

- 허수부 j로 표현

  ```python
  a.imag #허수부
  a.real #실수부
  ```



#### Bool

- 딕셔너리 키로 사용 가능함

`bool(입력값)`



#### None

```python
sorted()  #반환있음; 원본 냅두고 반환
.sort()   #반환없음; 원본만 변경; destructive 명령어.. 조심할것!!!!


```



#### 문자형(String)

```python
print(a+' '+b) == print(a, b)
'문자%s열%s'  %입력값( , )
```

```python
#f.스트링은 형식도 지정가능
import datetime
today = datetime.datetime.now()
print(today)
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')

#연산과 출력형식 지정가능
f'원주율이 {pi}일 때, 반지름이 {radius}인 원의 넓이는 {radius * radius * pi}다.'
```



#### 산술연산자

```python
divmod(a,b)   # 몫과 나머지를 튜플로 반환. - 를 변수에 직접 사용가능
(x,y)=(y,x)   # 변수 스왑하기
int('ab',20)  # 20진법의 ab를 10진법으로 바꾸기
```





#### 논리연산자

##### 단축평가 short circuit evaluation

```python
and  # a가 거짓이면 a리턴, 참이면 b리턴
or   # a가 참이면 a 리턴, 거짓이면 b 리턴  ★자주 씀
```



#### 기타연산자

`in` : 속해 있는지 확인

`is`  : 동일한 object인지 확인

```python
## id : -5부터 256 까지는 시스템 할당으로 미리 지정되어 있음(빈번한 사용)
a=-5
b=-5
a is b  # 미리 할당되어 있는 숫자는 True, 아니라면 False
```



### 연산자 우선순위

```python
1. ()을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +, - (음수/양수 부호)
6. 산술연산자 *, /, %
7. 산술연산자 +, -
8. 비교연산자, in, is
9. not
10.and
11.or
```

```python
(-3) ** 4  #81
-3 ** 4    #-81
```



## 기초형변환

### 암시적(implicit type conversion)

```python
True + 3     #4, True를 1로 취급
int+float    #float 화
int+complex  #complex화
```

### 명시적(explicit type conversion)

```python
string -> intger : 형식에 맞는 숫자만 가능

int(3.5) ## ValueError 발생
```



# 시퀀스형(sequence)

#### SET

```python
a-b  a.difference(b) 차집합
a|b  a.union(b) 합집합
a&b  a.intersection(b) 교집합
```

#### DICT

```python
key는 immutable한 모든 것이 가능 (불변값 : string, integer, float, boolean, tuple, range)
value는 list, dictionary를 포함한 모든 것이 가능
dic.keys() , dic.values() 는 리스트가 아님
```



##### data type 에 따른 구분

```python
시퀀스(ordered) : string, list, tuple, range()
unorderd : set, dictionary

mutable : list, set, dictionary
immutable : string, tuple, range()
```



# DAY 2

## MD 파일 관련

- `Ctrl+/` TYPORA에서 원본보기

- `Ctrl+Shift+v` or `우상단 돋보기아이콘` VS code에서 MD작성 후 프리뷰
- `'''파이썬` 하면 프리뷰에 syntax 하이라이트 됌..? 안되는데....   @@@@@@@확인@@@@@@



## Jupyter Notebook 관련

- esc + a / b : 셀추가

- dd : 삭제

- undo : edit 메뉴 이용



## Control of Flow, 반복문

조건표현식

```
true_value if <조건식> else false_value
```



for 와 if 는 블록베이스 스코프를 만들지 않음!!!

-->파이썬은 다른언어와 달리 for에서 쓴 변수도 전역변수화



```
enumerate(iterable, start=0)   # idx 시작 넘버링

for idx,menu in enumerate(lunch):   <-- 튜플 대 튜플 대응
    print(menu)
print(enumerate(lunch))  <--- enumerate object 주소가 출력
```



### DICT 제어

```python
for item in beside: # 키 출력
    print(beside[item])
 
for item in beside.keys():  # 키 출력
    print(item)   

for item in beside.values():  #  밸류 출력
    print(item)   

for item in beside.items():  #  튜플로 출력
    print(item)   

for k,v in beside.items():  #  pair 각각 출력
    print(k,v)   
```



```python
break # 바로 반복문 전체 종료
continue # 바로 뒤의 인자로 넘어가서 실행
pass # 지나치고 실행(뒤의 코드 실행됨)
```

```python
for ~ :
	break
else:   # break로 순환이 끝나지 않은경우에만 실행됌
```



## 함수

- 함수는 오직 하나의 값만 리턴 가능. 튜플도 하나의 객체로 취급

```python
dir(객체) # 변수와 메쏘드 전체보기
dir(__builtins__) # 내장함수 보기
```



### 기본값(default argument value)

`def 함수명(파라미터 = 디폴트):`  # 함수 정의 시 default argument value 설정

- 맨 뒤쪽에 와야함!

- mutable 이 디폴트로 설정되면, 반복 수행 시 꼬임 --> None 할당 후 조건문 설정

  ```python
  def add_book(book_list=None):
      if book_list is None:
          book_list =[]
      book_list.append('파이썬 베이직')
      return book_list
  ```



### 위치인자(positional argument)

- 기본형.. 정의한 위치에 사용

  

### 키워드 인자(keyword argument)

- 키워드가 맞으면 인자로 사용 (위치 무시)

  ```python
  def greeting(age, name='john'):
      print(f'{name}은 {age}살입니다.')
  
  greeting(name='철수', age=24)   # 동일결과 출력
  greeting(24, name='철수')       # 동일결과 출력
  greeting(age=24, '철수')        # 키워드 인자가 위치인자 앞에 오면 SyntaxError
  ```



### 위치 인자 언패킹

- `(*args)` : 임의의 갯수의 인자를 받기 위해서. 튜플형식으로 인자를 받음. 고정인자 뒤에 와야함.

```python
def my_max(*args): #정의 할때 사용 가능. 인자 받는 갯수 제한 X
    result = 0
    for idx, val in enumerate(args):
        if idx == 0:
            result = val
        else:
            if val > result:
                result = val
    return result
my_max(-1, -2, -3, -4)

my_max(*(-1,-2,-3,-4))  #변수 대신 바로 입력도 가능
```



### 키워드 인자 언패킹

- `(**kwargs)` : 정의되지 않은 인자 처리하기 위함. 딕셔너리 형식으로 인자를 받음. 맨뒤에 와야함

```python
def fake_dict(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f'{key}: {value}')
    print(', '.join(result))
```

```python
def user(username, password, password_confirmation):
    if password == password_confirmation:
        print(f'{username}님, 회원가입이 완료되었습니다.')
    else:
        print('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
        
my_account = {
    'username': '홍길동',
    'password': '1q2w3e4r',
    'password_confirmation': '1q2w3e4r'
}

user(**my_account)  # 변수에 인자로 넘기기
```



## 이름공간 및 스코프

```python
#스코프 분류
Local
Enclosed
Global
Built-in

global 변수 # 로컬내에서 전역변수 선언 가능
```





implementation 직접 찾아보면서 이해하기! 도 좋은 습관임.



map(함수,요소들) : 함수를 요소 하나하나마다 적용



# DAY 3

```python
# 빈도 카운트
import collections
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
print(collections.Counter(blood_types))
```

```python
blood_dict2 = dict()
for blood in blood_types :
   if blood_dict2.get(blood) :
       blood_dict2[blood] += 1
   else :
       blood_dict2[blood] = 1
```



```python
# 날짜구하기
from datetime import date, timedelta
(date.today()-timedelta(day=1)).isoformat().replace('-','')
#isoformat, strftime  /// timedelta를 시간으로도 가능.
```



### 재귀함수

반복문보다 성능 느림... 짜기 쉬움.

for문 여러번 도는것도 메모리 많이 잡아먹음..



# DAY 4

bash cp ~~파일 ~~위치     :배쉬파일 복사인가? 확인필요



## methods

`{  S or O  }.methods()`

### methods 구분

```
: destructive -- 원본 변경
: non destructive -- 원본 변경X   :  사용하려면 할당하는게 좋음   (대부분의 methods)

:return
:return X  -- 조심할것. # None type error, 거의 destructive methods
```



## for STRING

```python
.capitalize() # 맨앞글자만 대문자, 나머지 소문자
.title() # 첫글자, 공백/어퍼스트로피 이후 대문자. 나머지 소문자
.upper()
.lower()
.swapcase() # 대소변환

LIST.split('기준문자')   #미입력시 공백 기준 . 리스트화
'기준문자'.join(LIST)    #사용법 주의!
                       #' '.join(~.split())

.replace(old,new[, count]) # count지정시 해당갯수만큼

.strip([chars]) # 지정하지 않으면 공백(스페이스, 탭, 줄바꿈)  제거
.find('char')  # char의 첫번째 위치 반환
			   # 없으면 -1
.index('char') # char의 첫번째 위치 반환
               # 없으면 `ValueError`
    
#기타 참/거짓 반환 함수
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
```



## for LIST

```python
LIST.append('x')   #마지막에 1개 추가, 2개[iterable]는 불가 TypeError 발생

LIST += [iterable]   ==   LIST.extend([iterable])
caffe[len(LIST):] = 'x' or [iterable]  #  len 대신 -1하면 마지막 수정

.insert(i,'x')  #i에 `len(LIST)`하면 맨 뒤, #i에 -1하면 마지막 앞에(뒤에서 두번째) 들어감
                #길이를 넘는 인덱스는 맨 뒤에 붙음

.remove('x')  #인자 없으면 ValueError오류. 몇개인지 모르는 요소 다 없애려면 exept 처리 or 갯수 세는 반복문 필요

.pop(i)  #리턴이 있으면서도 destructive!!
		 #i 위치 삭제하고 반환,  i 없을시에는 제일 뒤에꺼

del LIST[2:]  #이렇게도 삭제 가능

.index('x') #찾아서 인덱스 반환,  없으면 ValueError

.count('x') #갯수확인

.sort() #destructive, 리턴없음(None)

.reverse() #반대로 뒤집기

.clear() #모든항목 삭제
```



## COPY (pythontutor 활용 추천)

mutable : List, Set, Dictionary    ---  주소만 복사, 값 공유

immutable : Tuple, Range, String, Number   --- 값을 복사해서 새로 생성



- 리스트 복사하기

  - shallow copy

    - num3=num[:]
    - num4=list(num)

  - ​	deep copy

    - ```python
      import copy
      copy.deepcopy()
      ```

    - recursive 하게 직접 짜기?



## List comprehension

```python
listcomp=[i**3 for i in numbers if i%2==0]

#피타고라스 정리
pit=[(x,y,z) for x in range(1,50) for y in range( x+1, 50) for z in range(y+1,50) if x**2+y**2==z**2]
print(pit)

#모음삭제
words = 'Life is too short, you need python!'
b='aeiouAEIOU'   # == ['a', 'e', 'i', 'o', 'u', 'A',...]
rrrrrr=[i for i in words if i not in b]
z=''.join(rrrrrr)
print(z)
```



set으로 단어 카운트?

# Dict

```python
.pop(key[, default]) #키 있으면 제거하고 값 반환, 없으면 default 반환
					 #디폴트 없이 키가 없으면 KeyError 발생
    
.update(dict) #해당 key와 value로 덮어씀
              #딕셔너리를 넣거나 언패킹된 상태`(apple='사과')`로 넣어야함   **kwargs

.get(key[, default])  # 없으면 None 반환  #인덱싱은 에러발생


```

```
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='사과아', bana='바나나')
my_dict
```



## DICT comprehension

```python
cubic_dict = {i:i**3 for i in range(1,10)}
print(cubic_dict)


dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

hell={i:dusts[i] for i in dusts if dusts[i]>80}
{key:value for key,value in dusts.items() if value>80}

ccc={key:'나쁨' if value > 80 else '보통' for key,value in dusts.items()}
bbb= {key:'매우나쁨' if value > 150 else '나쁨' if value> 80 else '보통' if value>30 else '좋음' for key,value in dusts.items()}
```



## SET

```python
.add('x')
.update([iterable])
.remove('x')  #없으면 KeyError
.discard('x') #없어도 무관
.pop() #임의 제거 후 반환
```



# 표만들기  `|내용|내용|`

| -      | String | List                                                         | Dictionary                                                   | Set                                                          |
| ------ | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Create |        | .append('x')<br />.extend([iterable])<br />.insert(i,'x') i초과하면 제일 뒤에 추가 | .update(dict)                                                | .add('x')<br />.update([iterable])                           |
| Read   |        |                                                              | .get('key'[, default]) 없으면 None<br />[ ]인덱싱은 없으면에러발생 |                                                              |
| Update |        |                                                              |                                                              |                                                              |
| Delete |        | .remove('x') 없으면 ValueError<br />.pop(i)  i없으면 제일 뒤에꺼.리턴O, destructive | .pop('key'[, default]) 디폴트 없으면 KeyError                | `remove('x')` 없으면 KeyError<br />`discard('x')` 없어도 무관<br />`pop()` no input, 랜덤삭제, 리턴O |



## for iterable

```python
.map(함수, iterable)  #모든 원소에 함수 적용후 리턴
                     #리턴은 map_object
                     #  함수호출하지 않도록 주의 `str // not str()`
                     #없는함수는 만들어서 써야함
                     #인자가 하나인 경우에만?  두개이상도 가능은한데 어려움
    

.zip(*iterable) #복수의 iterable을 모아줌
                #리턴은 zip_object
                #길이가 다르면 가장 짧은 iterable 기준으로 생성
        
        #길이가 긴거에 맞출수도 있지만 사용할일 없음
        from itertools import zip_longest
		list(zip_longest(num1, num2, fillvalue=0))
        

.filter(함수, iterable)  #함수결과 참인것만 반환
```

```python
#짝수 추출하기
numbers=list(range(1,31))
evens=[]

#for 버전
for num in numbers:
    if not num%2:
        evens.append(num)
        
#comprehension 버전        
evens=[num for num in numbers if not num%2]

#filter 버전
list(filter(even,numbers))
```



# DAY 5

 .csv : 콤마로 구분.   기본 텍스트이므로, ' ' 안써도 됌

프로젝트 진행.

VS code에서 excel viewer 설치!



```python
# lunch.csv 데이터저장
with open('lunch.csv', 'w', encoding='utf-8', newline='') as f:
    for k,v in lunch.items():
        f.write(f'{k} : {v}\n')

#',' join을 통해 string 만들기
with open('lunch.csv', 'w', encoding='utf-8', newline='') as f:
    for item in lunch.items():
        # f.write(','.join(zip(k,v))
        f.write(','.join(item) + '\n')

#csv writer 이용
import csv  #csv 파일 편집
with open('파일.csv', 'w', encoding='utf-8') as f:
	약어함수명 = csv.writer(f)
	for item in 딕셔너리.items():
		csv_writer.writerow(item)
		
#Dictwriter 이용 : key를 fieldnames, value를 row에 매핑하는 객체 생성
with open('파일.csv', 'w', encoding='utf-8') as f:
	fieldnames = ['column1', 'column2']     #첫행 열이름 - 딕셔너리 구조에서 키 역할
	writer = csv.DictWriter(f, fieldnames=fieldnames) #DictWriter 선언
	writer.writeheader()                              #fieldnames 첫행에 입력하기
	writer.writerow({'name':'john', 'major':'cs'})    
    writer.writerow(딕셔너리)           #fieldnames 를 키로, 딕셔너리 형태로 넣어야함

DictWriter(f, fieldnames[, restval='', extrasaction='raise', dialect='excel', *args, **kwds])
  # restval(디폴트='') = fieldnames 빠졌을때 기록될 값
  # extrasaction(디폴트='raise') = fieldnames에 없는 키값 입력이 들어오면, ValueError
                                 #'ignore' 설정시, 그냥 무시

    
#DictReader : 각 row의 정보를 키가 fieldnames로 정의된 dict로 매핑하는 객체 생성
with open('파일.csv', 'r', encoding='utf-8') as f:
    reader=csv.DictReader(f[, fieldnames=None, restkey=None, restval=None, dialect='excel', *arg, **kwds)
                       #fieldnames 생략하면 첫행을 key값으로 씀
                       #자료에 fieldnames보다 필드가 더 많으면,
                          # 나머지는 리스트 형태로 restkey(디폴트 None) 필드에 저장
                       #자료에 fieldnames보다 필드가 적다면,
                          # restval(디폴트 None)으로 채워짐 (완전히 빈 행은 건너뜀)
	for row in reader:
        print(row['key1'], row['key2'])
```



프로젝트.... 1주차

```python
#shallow copy 조심
a = {'1': 32}
b={}
b.update({'1':a})
a.clear()    ## 여기를 a={} 로 선언하면 원본은 남아서, b는 유지
print(b)
```