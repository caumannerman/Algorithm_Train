#list

#벡터같이 기능들이 강력해 편함.
a=[1,2,3,4,5]

b=[1]*3
#[1,1,1]됨

#인덱싱 (일부분 추출)
a[1:4]
1번 인덱스부터 3번 인덱스까지 잘라옴

#리스트 컴프리헨션
a=[ i  for i in range(10)]

b=[i for i in range(20) if i%2 == 1]

"""array =[]
for i in range(1,20):
    if i%2 == 1:
        array.append(i)
        이와 같은 4줄이 1줄로 줄어드는 것
"""

c= [i**2 for i in range(1,10)]

#2차원 리스트******

array = [[0]*m for _ in range(n)]

arr =[[0]*m]*n 하면 똑같은 리스트가 n개 복사되는 것이기 때문에, 주솟값 공유. 따라서 하나만 바꿔도 모두 바뀜

append(), sort() reverse(), insert(), count(), remove()

result =[i for i in arr1 if i not in arrr2] ## 컴프리헨션 중요!!

%% 문자열 수정 불가능

%% 튜플은 리스트에 비해 공간 효율적. + 한 번 선언된 값 변경 불가능

&& 튜플을 사용하기 좋은 경우
1. 서로 다른 성질 데이터 묶어 관리 ( 최단경로에서 (비용, 노드번호) 형태로. 튜플 자주사용
2. 변경불가이므로 키 값으로 사용됨
3.메모리 효율 따질때


$$ 세번째 자료형   "사전" - ket, value를 쌍으로 가짐
Immutable한 자료형을 key로 사용 가능
a["key"]="value"로 추가
aa= dict()로 선언
ss=aa.keys()
ss=aa.values()로 키, 값만 배열 늒미으로 사용가능

$$네번 째 집합 set 자료형 {} 사용
data = {1,2,3} 혹은 data = set([1,1,2,3,4,4,5])
data.add(4)
data.update((5,6))
data.remove(3)

____________________________________________________________________________________
표준 입출력

input() 한줄로 입력
map() 리스트의 모든 원소에 각각 특정한 함수를 적용

data = list(map(int, input().split()))      모두를  int로 바꿔주는것!!



input보다 빠른게 sys.stdin.readline()이다!! 근데 \n이 붙어서 저장되므로 rstrip() 같이써:
sys.stdin.readline().rstrip() 이렇게!!

표준 출력
print() ,로 구분하여  띄어쓰기로 구분하여 출력가능 - 기본적으로 줄바꿔줌
포멧해서 스트링 출력하기
a=1
print(f"정답은{a}입니다")   이렇게!!!






















