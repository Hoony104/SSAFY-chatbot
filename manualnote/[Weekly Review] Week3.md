유튜브! 3blue1brown  선형대수 / 비트코인?/ e   / sha256

vi. hello.py

`cp 파일명 ~/폴더명/` : bash에서 파일 복사하기

# [Weekly Review] Week3

주석은 docstring으로 대체하여, 한눈에 알아보기 쉽게 짜는게 추세.

## Module

- 함수 / 변수 / 클래스를 모아놓은 파일

- 파이썬은 모든 .py 파일을 모듈로 인식!   

- 커널스타트 시점에 모듈을 로드함.  수정저장 후에는, 리스타트 필요!

  ```
  소스코드를 github 가면 볼수 있음 (github 함수 python 구글검색)
     --> 표준 정리양식 보면서 참고하면 좋음
  큰 문제를 추상화, 단위로 쪼개는게 좋음   이게 굉장히 중요한 능력
  모듈화- 리눅스의 성공요인?
  ```

```python
#모듈 불러오기
import 모듈이름
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *
```

```python
if __name__=='__main__':   # 모듈로 불러올때는 거짓이되어 실행안됌.
                           # 인터프리터에서 켜서 사용할때는 참이되어 실행가능
                           
__name__  : 모듈 불러오기시 값은 파일명.  직접켜면 값은 __main__
```



## 패키지

- 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리
- `__init__.py` 파일 : 파이썬이 디렉터리를 패키지로 인식하게 하기 위해서 필요(V.3.3부터는 없어도 됨)
- `from 모듈명 import 어트리뷰트  #어트리뷰트 = 변수+함수`
- `__init__.py`  안에 있는 함수는 바로 실행됌

```python
# game(폴더)-sound(폴더)-echo(.py)-echo_test(func.) 라 할때
import game.sound.echo
from gam.sound import echo
from game.sound.echo import echo_test

#불가능한 문법
import game (X)
import game.sound.echo.echo_test (X)


#폴더가 from의 마지막에 오면
from game.sound import *
# 이렇게 사용하려면 해당 디렉토리에 __init__.py 파일에 __all__변수를 설정하고 import할수 있는 모듈을 정의해주어야함.

#모듈이 from의 마지막에 오면,
from game.sound.echo import * #__all__과 상관없이 무조건 import.

```

```python
# from 모듈 import *   : 모두 가져오기
  ## 너무 무겁다.  변수명 충돌... 임포트 순서가 있지만,, 프로그래밍 난해해짐
    
# from 모듈 import 어트리뷰트 as ~
form bs4 import BeautifulSoup as bs
```



### import 서치 순서  --- 빌트인과 같은 파일명 만들면 안됌!

```python
1.내장모듈
2.sys.path에 정의된 디렉토리 #아래 참고
   - 파이썬 모듈 실행되는 디렉토리
   - 파이썬 PATH 환경변수에 정의된 디렉토리
   - 파이썬과 함께 설치된 기본 라이브러리
```

```python
#환경변수 경로 확인하기
import sys
sys.path
```

매직메쏘드? 파이썬 시스템에서 상속된 속성들.  `dir(갓만든함수)`



## 숫자 관련 함수

```python
#import math
.pi
.e
.ceil('r')
.floor('r')  # 아래 참고(음수에서의 차이)
.trunc('r')  # 아래 참고(음수에서의 차이)
.copysign('x','y') #y의 부호를 x에 적용
.fabs #float 절대값, 복소수는 오류발생
.factorial('x') # 팩토리얼
.fmod('x','y')  # float 나머지 계싼
.fsum([iterable]) #float 합
.modf('x')  # 소수부 정수부 분리
.pow('x','y')  #float 반환
    ### 내장함수인 pow('x','y') == x**y와는 다름, 정수라면 정수반환
.sqrt('x')
.exp('x')
.log(x[, base])  == .logbase(x)
삼각함수류..(sin, asin, sinh, ashinh ~~ )
```

```python
import math
math.trunc(-pi)   #-3  버림
math.floor(-pi)   #-4  내림
  
    수학적으로... 소수부는 양수여야 한다? -3.5 = -4 + 0.5
```

`.conjugate()  #켤레복소수` 참고

```python
#import random
random.random()
random.randit(min,max)   ### max도 포함
random.seed('seed')   # 랜덤시드 고정
random.shuffle(LIST)
	# 컴퓨터에서는 랜덤을 모사한 것.
    # hash~?  sha1 정도는 돌려야 균일한 랜덤분포?
    # git 또한 sha1 사용해서 status 체크
```



```python
#import datetime    #형식이나 속성 지정 가능. %Y / .year 등
datetime.datetime.now()
datetime.datetime.today()
datetime.datetime.utcnow()
	now.month
    now.weekday()
datetime.timedelta(days=3) 
```



## Errors and Exceptions

- ### try & except 

  모든 케이스를 조건문으로 커버하기 어려움. 엣지케이스 처리를 쉽게 하기 위함.

```python
try:
	codeblock1
except (예외1, 예외2) as e:  # 에러코드 출력하기 위함
	codeblock2
    print(f'{e} 에러발생 ')
    
except: # except Exception: # 모든 예외 처리 # 마지막에 하나 넣어서 오류 예방
	codeblock3 # 마지노선
    
else:     # excpet 발생 안할때
    codeblock4
    
finally:  # 다 하고나서 실행 필요할때(에러발생 하든 안하든)
    codeblock5 
    
raise 에러명('메시지')    #특정 데이터 거를때 유용
```



- ### assert

```python
assert Boolean expression, 'errormessage' #거짓일 경우 에러메시지 출력
```

​	TDD(Test Driven Develope) 에 많이 씀.  Edge case 먼저 다 가정하고, 코딩시작



# OOP

- Object-Oriented Programming : 기존의 절차적 프로그래밍에서 탈피.  

```python
클래스(Class)
	종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다
	클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.

인스턴스(instance)
	클래스의 인스턴스/객체(실제로 메모리상에 할당된 것)이다.
객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.
	객체의 행위는 클래스에 정의된 행위에 대한 정의(메서드)를 공유함으로써 메모리를 경제적으로 사용한다.

속성(attribute)
	클래스/인스턴스 가 가지고 있는 속성(값).   (.real/.image    호출()이 없음)

메서드(Method)
	클래스/인스턴스 가 할 수 있는 행위(함수)   (.conjugate())
```

### 클래스

```python
클래스 또한 객체
공간은 **지역스코프** 로 사용됨   (def도 지역스코프임)
정의된 어트리뷰트 중 변수는 멤버변수로 불리운다.
정의된 함수는 메서드(method)라고 불린다
카멜케이스 : 띄어쓰기 단위로 대문자가 관례
```

```python
# str(self) or print(self) 입력시 출력. 사용자가 알아보기 쉬운 정도로만 나타냄
def __str__(self):
    return 'str 이라고!'

#self 입력시 출력. 시스템이 해당 객체를 인식할 수 있는 공식적인 '문자열'로 나타냄
def __repr__(self):
    return 'repr 이라고!'
```

### 인스턴스

```
인스턴스 객체는 ClassName()을 호출함으로써 선언된다.
인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.
인스턴스 => 클래스 => 전역 순으로 탐색을 한다.
```

### self

```
C++ 혹은 자바에서의 this 키워드와 동일함.
특별한 상황을 제외하고는 무조건 메서드에서 self를 첫번째 인자로 설정한다.
메서드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어있다.

다른걸로 바꿔써도 무방(예약어 아님, 관례)
```

### 클래스-인스턴스

```
클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다.
인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.
인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.
즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 => 클래스 순으로 탐색을 한다.
```



### 생성자의 필요성

```python
클래스 멤버변수에 mutable인 리스트를 넣으면 해당주소를 가리킴.
기본적으로 인스턴스는 속성을 재정의(새로운 mutable 생성)하기 전에는, 클래스의 속성을 공유함
따라서 인스턴스에서 재정의 없이,  mutable 속성을 변경시 클래스 속성 자체가 변경
(새로운 주소를 가리키게 재할당 하면 인스턴스만의 객체가 됨)

__init__  필요성
```

## 생성자, 소멸자

```python
def __init__(self, args):   #추가인자 받을수 있음
	pass
def __del__(self):   # 호출함수가 아님, 추가인자 받을 수 없음
	pass

#소멸자 사용시 문법 주의
del self  #O
self.__del__  #X
```

```python
#코딩 참고. 같은 결과.
try:
    return self.data[-1]
except:
    return None

if self.data:
    return self.data[-1]     #else는 자동으로 None

#함수내용에 아무것도 없으면 pass라도 넣어야 오류 안남
```



## 클래스 메서드, 스태틱 메서드

```python
#클래스 메서드 : 클래스, 인스턴스 모두 접근 가능, 클래스와 관련된 메서드들.
class 클래스명:
	@classmethod
	def 클래스메서드명(cls, arg1, arg2, ...):

#스태틱 메서드 : 해당클래스가 쉐어는 하되, 클래스와 연관없는 메서드들..
class 클래스명:
	@staticmethod
	def 스테틱메서드명(arg1, arg2, ...):    #호출될때 자기자신이 없음.
```

```python
#인스턴스메서드는 클래스메서드/스태틱메서드에 접근가능
## BUT 추천X 가능하지만 사용하진 않는다.
id(인스턴스.class_method()) == id(클래스)  #True
인스턴스.class_method() == 클래스  ##True
인스턴스.static_method()  ## 함수지정한대로 출력
```

```python
#클래스메서드도 모두 접근가능
##BUT 인스턴스 추천 X. 
#클래스 자체(cls)와 그 속성에 접근 필요가 있다면 클래스메서드로 정의
#필요없다면 스태틱메서드로 정의    ex)계산기
```

```python
#클래스메서드는 데코 떼면 인스턴스메서드로 취급됌
#스태틱메서드는 데코 떼도 동일하나, 따로 스태틱메서드만 모아서 알려주는 명령어가 있음
```

```python
연산자 오버로딩 가능
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__

#한쪽방향만 정의하면, 반대방향도 인식함.
#다른 기능들도 연계하여 사용가능해짐. 리스트에서 sorted() 등
```

```python
#정의 예시
	def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self,other):
        return self.age==other.age
```

## 상속

```python
#정의 - 상속 클래스를 지칭하는 용어들
class DerivedClassName(BaseClassName):
class SubClass(SuperClass):
class ChildClass(ParentClass):
```

## super() 

- 자식클래스에 메서드 구현 시, 오버로딩 中 상위 클래스의 내용을 가져올때

```python
class Student(Person):
    def __init__(self,name,age,idcard):
        super().__init__(name,age)   ##Person.__init__
        self.idcard=idcard
#탐색순서는 인스턴스 -> 섭클래스 -> 수퍼클래스 -> 전역
```



`__str__`   객체를 str으로 변환할때 나타는거

`__repr__`  객체를 어떻게 나타낼지.. 객체 자체를 출력하면 나오는 거

​     repr을 정의하면 str 정의 안해도 나옴



## 프로젝트 실습

네이버 api  : timeout 존재.

```
# sleep.   `import time`
import time
time.sleep()  #sec 단위, 실수 입력가능
```

