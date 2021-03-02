"""방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# 출력 : 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    for i in range(1,len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)
result = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)