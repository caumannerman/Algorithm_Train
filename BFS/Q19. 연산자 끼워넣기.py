"""N개의 수로 이루어진 수열 A1,A2,A3,....An이 주어진다. 또, 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가 주어진다.
연산자는 덧셈(+) 뺄셈, 곱셈(X), 나눗셈으로만 이루어진다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있는데, 이 때 주어진 수의 순서를 바꾸면 안된다.
예를 들어 6개의 수로 이루어진 수열이 1,2,3,4,5,6이고, 주어진 연산자가 덧셈(+)2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개인 경우는 총 60가지의 식을 만들 수 있다.에

식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행해야한다. 또 , 나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤, 몫을 취하고, 그 몫을 음수로 바꾼것과 같다.
이에 따라서 위의 식 4개의 결과를 계산해보면 다음과 같다.
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하라."""
# 첫 째 줄에 수의 개수 N(2~11)이 주어ㅣㄴ다.
# 둘 째 줄에 A1,A2,A3....An이 주어진다 (1<= Ai <= 100)
# 셋 째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 갯수, 뺄셈의 갯수, 곱셈의 갯수, 나눗셈의 갯수이다.

# 출력 - 첫 째 줄에 만들수 있는 식의 결과의 최댓값을 출력
# 둘 째 줄에는 최솟값을 출력
# 최대, 최솟값이 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 동일 범위에 있다.


import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add,sub,mul,div = list(map(int ,input().split()))

max_result = -int(1e9)
min_result = int(1e9)

def dfs(level, result, add,sub,mul,div):
    if level == n-1:
        global max_result, min_result
        max_result = max(max_result,result)
        min_result = min(min_result, result)
        return

    if add:
        dfs(level+1, result + data[level+1], add-1, sub,mul,div)
    if sub:
        dfs(level + 1, result - data[level+1], add, sub-1, mul, div)
    if mul:
        dfs(level+1, result * data[level+1], add, sub, mul-1, div)
    if div:
        if result >= 0:
            dfs(level+1, result // data[level+1], add, sub, mul, div-1)
        else:
            dfs(level+1, -((-result)//data[level+1]) , add, sub, mul, div-1)
dfs(0, data[0], add, sub, mul, div)
print(max_result)
print(min_result)