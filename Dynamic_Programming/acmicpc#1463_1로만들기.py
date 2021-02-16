"""정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오."""

# 입력 : 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
# 출력 : 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 틀렸던 이유: 1,2,3이 입력으로 들어왔을 경우를 코드의 앞쪽에 처리해주지 않았었다.
# 22 21 7 6  2 1
# 22 11 10 5 4 2 1
# 22 11 10 9 3 1
n = int(input())

if n == 2 or n == 3:
    print(1)
elif n == 1:
    print(0)
else:

    count = 0

    dpTable = [0] * (n + 1)

    dpTable[2] = 1
    dpTable[3] = 1

    for i in range(4, n + 1):
        temp = []
        if i % 3 == 0:
            temp.append(dpTable[i // 3] + 1)
        if i % 2 == 0:
            temp.append(dpTable[i // 2] + 1)
        temp.append(dpTable[i - 1] + 1)
        dpTable[i] = min(temp)

    print(dpTable[n])