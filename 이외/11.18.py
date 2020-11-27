

기타 연산자

in
not in
pass ( 아무것도 처리하고싶지 않을때.  조건문 elif같은 곳에서 사용!)

조건문에서 실행 코드 한 줄이면 if score >=80: result = "success" 와 같이 한 줄에 작성가능
%%%%조건부 표현식은 if,else를 모두 한 줄에 표현가능 result = "success" if score >=80 and ~   else "Fail"


^^ 반복문 ^^
while 조건:
    ~~~

for 변수 in 리스트 혹은 튜플:
    ~~~
순회할때는
for i in range(1,10):
    ~~~ 이렇게!!

continue 똑같음
break도 똑같음

함수 정의하기
    def 함수명(매개):
       실행 소스코드
       return 반환값

전역변수를 함수 안에서 사용하고싶으면, global 변수이름
써줘야 해당 전역변수에 적용이된다:


$ 파이썬도 여러개 반환 하는 함수 가능!!!!!

def hamsoo(a,b):
    daf=a+b
    ddd=a-b
    kkk=a*b
    lll=a/b
    return daf,ddd,kkk,lll
사용 시, a,v,c,d=hamsoo(1,2) 이렇게

$람다 표현식
(lambda a,b:a+b)(3,7)  이게 더해주는 람다 add함수

sum()
eval()
sorted([1,2,3,4,5],reverse=True)

