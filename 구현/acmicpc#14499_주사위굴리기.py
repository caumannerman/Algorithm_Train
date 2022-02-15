import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
op = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 서,밑면,동쪽,윗면,앞(내기준) ,뒤
dice = [0, 0, 0, 0, 0, 0]


def rollDice(dir):
    # 동
    if dir == 1:
        temp = dice[0]
        for i in range(3):
            dice[i] = dice[i + 1]
        dice[3] = temp
    # 서
    elif dir == 2:
        temp = dice[3]
        for i in range(3, 0, -1):
            dice[i] = dice[i - 1]
        dice[0] = temp
    # 남
    elif dir == 4:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = dice[5]
        dice[5] = temp
    # 북
    else:
        temp = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp


for i in op:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    rollDice(i)
    x, y = nx, ny
    print(dice[3])
    if data[x][y] == 0:
        data[x][y] = dice[1]
    else:
        dice[1] = data[x][y]
        data[x][y] = 0
