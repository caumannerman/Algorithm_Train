"""0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 -> 1, 1 -> 0)"""

# 입력 : 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
# 출력 : 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.


# 리스트 컴프리핸션 -
# 2차원 배열을 선언할 때는 [[True] * m for _ in range(n)] 과 같이
# 2차원 배열 순회시, 뭉뚱그려서 전체가 True인지 아닌지만 알면 될 때는, 2중for문보다는, 행 갯수만큼 for문 돌며 리스트 컴프리핸션으로


import sys

input = sys.stdin.readline


def flop(arr, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr[i][j] = not arr[i][j]


def check(arr, x, y):
    for i in range(x, n):
        if all(arr[i][y:]):
            continue
        else:
            return False
    return True


n, m = map(int, input().split())
data1 = []
data2 = []
for _ in range(n):
    data1.append(list(map(int, input().rstrip())))
for _ in range(n):
    data2.append(list(map(int, input().rstrip())))

diff = []

for i in range(n):
    diff.append([True if data1[i][j] == data2[i][j] else False for j in range(m)])


if n < 3 or m < 3:

    for i in range(n):
        if all(diff[i]):
            continue
        else:
            print(-1)
            exit()
    print(0)
    exit()

count = 0

for i in range(n - 2):
    for j in range(m - 2):
        if not diff[i][j]:
            flop(diff, i, j)

            count += 1

if check(diff, 0, 0):
    print(count)
    exit()

print(-1)