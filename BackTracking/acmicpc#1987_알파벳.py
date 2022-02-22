import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

result = set([data[0][0]])


def dfs(x, y, level):
    global count
    count = max(count, level)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if data[nx][ny] not in result:
            result.add(data[nx][ny])
            dfs(nx, ny, level + 1)
            result.remove(data[nx][ny])


dfs(0, 0, 1)
print(count)