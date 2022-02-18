import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = True
    idx = 0
    while len(q) > idx:
        for i in range(2):
            nx = q[idx][0] + dx[i]
            ny = q[idx][1] + dy[i]
            if nx >= n or ny >= n:
                continue
            if l <= abs(data[nx][ny] - data[x][y]) <= r:
                q.append((nx,ny))
                visited[nx][ny] = True
                idx += 1
    if len(q) > 1:
        temp = 0
        for (qx, qy) in q:
            temp += data[qx][qy]
        temp //= len(q)
        for (qx, qy) in q:
            data[qx][qy] = temp
        return True
    return False


result = 0
while True:
    tick = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j):
                    tick = True
    if tick:
        result += 1
        continue
    break
print(result)