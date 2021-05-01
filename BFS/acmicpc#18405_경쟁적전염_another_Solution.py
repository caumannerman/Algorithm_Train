import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
virus = []
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
virus.sort()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    for i in range(len(virus)):
        q.append((0, virus[i][1], virus[i][2]))
    while q:
        now_s, now_x, now_y = q.popleft()
        if now_s == s:
            break
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[now_x][now_y]
                q.append((now_s + 1, nx, ny))


bfs()

print(graph[x - 1][y - 1])