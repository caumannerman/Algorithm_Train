import sys

input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
data = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(r):
    data.append(list(input().rstrip()))

bv = (-1, -1)
gsdc_x = -1
gsdc_y = -1
water = []
# 초기 S, D, * 위치 알아내기
for i in range(r):
    for j in range(c):
        if data[i][j] == 'D':
            bv = (i, j)
        elif data[i][j] == 'S':
            gsdc_x = i
            gsdc_y = j
            data[i][j] = '.'
        elif data[i][j] == '*':
            water.append((i, j))

q_water = deque(water)
q_gsdc = deque([(gsdc_x, gsdc_y)])

visited = [[False] * c for _ in range(r)]
visited[gsdc_x][gsdc_y] = True

time = 0
tick = False

while True:
    # 한 턴의 물 이동 q_water 갯수만큼
    for _ in range(len(q_water)):
        now_x, now_y = q_water.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if data[nx][ny] == '.':
                data[nx][ny] = '*'
                q_water.append((nx, ny))
    time += 1
    for _ in range(len(q_gsdc)):
        now_x, now_y = q_gsdc.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if data[nx][ny] == 'D':
                print(time)
                exit()
            elif data[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                tick = True
                q_gsdc.append((nx, ny))
    if not tick:
        print("KAKTUS")
        exit()
    tick = False
