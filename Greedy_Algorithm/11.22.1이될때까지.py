''' 어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나를 선택하여 수행한다.
        1. N에서 1을 뺀다.
        2. N을 K로 나눈다
        이 과정을 통해, N을 K로 만드는 최소 횟수를 구하는 프로그램을 작성하세요.'''
# 첫 쨰 줄에서 N 과 K가 ' '으로 구분되어 입력된다 & 첫 째 줄에 수행해야하는 횟수의 최솟값을 출력한다.

n, k = map(int, input().split())

count = 0

while n >= k:
    while n % k != 0:
        n -= 1
        count += 1

    n //= k
    count += 1


while n > 1:
    n -= 1
    count += 1

print(count)

