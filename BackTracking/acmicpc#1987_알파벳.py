import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input().rstrip()))

visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
visited[0][0] = True
result = set([data[0][0]])

def dfs(x,y):
    tick = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visited[nx][ny] and data[nx][ny] not in result:
            tick = True
            visited[nx][ny] = True
            result.add(data[nx][ny])
            dfs(nx,ny)
            result.remove(data[nx][ny])
            visited[nx][ny] = False
    if not tick:
        global count
        count = max(count, len(result))
dfs(0,0)
print(count)

