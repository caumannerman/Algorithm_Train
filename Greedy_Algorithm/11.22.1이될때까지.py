''' 어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나를 선택하여 수행한다.
        1. N에서 1을 뺀다.
        2. N을 K로 나눈다
        이 과정을 통해, N을 K로 만드는 최소 횟수를 구하는 프로그램을 작성하세요.'''
# 첫 쨰 줄에서 N 과 K가 ' '으로 구분되어 입력된다 & 첫 째 줄에 수행해야하는 횟수의 최솟값을 출력한다.
# 반복문을 최대한 제거하였다.

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
result = 0
while n >= k:
    if n%k != 0:
        result += n % k
        n -= n %k

    result += 1
    n //= k

if n == 1:
    print(result)
else:
    print(result + n-1)


