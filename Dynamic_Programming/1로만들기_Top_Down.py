'''정수 X가 주어질 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
       1. X가 5로 나누어떨어지면, 5로 나눈다.
       2. X가 3으로 나누어떨어지면, 3으로 나눈다.
       3. X가 2로 나누어떨어지면, 2로 나눈다.
       4. X에서 1을 뺀다.

       정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.'''
dpTable = [0]*300001
x = int(input())
arr = (2,3,5)

def tddp(n):
    if n == 1:
        return 0
    if n == 2 or n == 3 or n == 5:
        return 1
    if dpTable[n] != 0:
        return dpTable[n]
# 이 아랫줄 tmp = [dpTable[n-1]]과 같이 초기화해주면 안됨. 그럴 경우, 나중에 하위 계산에서 1,2,3,5는 우리가 함숫값으로 갖고오지, dpTable상에는 제대로 된 값이 아닌
# 0으로 채워져있기 때문.
    tmp = [tddp(n-1)]
    for i in arr:
        if n % i == 0:
            tmp.append(tddp(n//i))
    dpTable[n] = min(tmp) + 1
    return dpTable[n]


print(tddp(x))


# Top-Down Dynamic-Programming에서  기억해야할 점
''' 1. dp-Table 만들기 (최대 크기)
    2. if문을 이용,  기반이 되는 인덱스들이 나오면 해당 값을 return
    3. if문을 한 번 더 사용하여, dp[n]이 0이 아니면,(즉, 이미 계산한 적이 있다면 ) dp[n]으로 return
    4. dp[n]을 아직 모른다면, 재귀함수를 이용하여 문제에 맞게 return'''

#배운 점 :
# map으로 자주 사용해왔던 int()뿐 아니라 사용자 정의 함수도 원소마다 다 적용시켜줄 수 있다.
# map()을 통해 나온 결과는 데이터상에만 적용되어 저장되므로, 사용하려면 list(map(~~~))과 같이 밖에 리스트 혹은 set 등을 씌워주어야 한다.
# map 객체에는 append할 수 없다. # min(map객체) 는 가능

