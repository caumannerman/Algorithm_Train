import sys

input = sys.stdin.readline
# 경로가 있는지 없는지로 순위를 매기는 것이다!!
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == k or j == i:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
resultArr = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            resultArr[i] += 1
            resultArr[j] += 1
print(resultArr.count(n+1))