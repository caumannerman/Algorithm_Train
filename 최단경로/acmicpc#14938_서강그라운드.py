import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == i or j == k:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            print(i, item[j])
            temp += item[j]
    result = max(result, temp)
print(result)