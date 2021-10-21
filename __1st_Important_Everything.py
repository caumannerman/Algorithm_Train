import sys

input = sys.stdin.readline
from collections import deque  # bfs
import heapq  # ㄷㅏ익스트라

INF = int(1e9)  # 다익스트라

n = 100
graph = []
data = []
visited = [False] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# 이진탐색
def bs(target):
    start = 0
    end = len(graph)
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

# DP

# Dijkstra
import heapq
n, m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# Floyd-warshall
# 인접행렬 구성 , 대각선 원소들 0으로 초기화
#
INF = int(1e9)
distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == i or j == k:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# union&find , 서로소, 싸이클, Kruskal
parent = [i for i in range(n+1)]
def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
---------- Kruskal---------------------
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a,b))
edges.sort()
result = 0

for cost, a, b in edges:
    if find(parent,a) != find(parent, b):
        union(parent, a, b)
        result += cost
    else:
        continue

# 간선 (거리,a,b)로 리스트에 모두 담고, sort()
# 하나씩 pop 하며, 싸이클이 안 생길 경우에만 union 하면서 Kruskal Algo 수행 가능

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    indegree[b] += 1
# 간선 입력받으며, indegree 수정
result = []

def topology():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

# backtrackint
#Two pointer
# bellman
#segment Tree