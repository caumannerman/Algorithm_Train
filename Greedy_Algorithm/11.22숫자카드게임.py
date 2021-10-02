'''여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
게임의 룰
    1. N행, M열의 형태로 카드가 놓여있다.
    2. 카드를 선택할 '행'으로 선택을 하고, 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다.
    3. 최종적으로 가장 높은 숫자를 뽑을 수 있도록 전략을 세워야한다.
   '''
# 첫 번 째 줄에서 N, M을 ' '으로 구분하여 입력받고, 둘 째 줄에서부터 '한 행'씩 총 M번 입력받는다.
#룰에 맞게 뽑을 수 있는 가장 높은 숫자를 출력한다.
import sys
input = sys.stdin.readline
n ,m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

minmax = -1

for i in range(n):
    temp = min(arr[i])
    if temp > minmax:
        minmax = temp

print(minmax)

# 21.10.2 풀이

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(min(list(map(int, input().split()))))

print(max(data))
