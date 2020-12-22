from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = []

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(start, visited):
    visited.append(start)
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited

def bfs(start):
    visited = [start]
    q = deque([start])
    while q:
        now = q.popleft()
        for i in range(len(graph[now])):
            if graph[now][i] == 1 and (i not in visited):
                visited.append(i)
                q.append(i)
    return visited

print(*dfs(v, visited))
print(*bfs(v))