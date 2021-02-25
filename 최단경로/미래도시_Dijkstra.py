import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance
d0 = dijkstra(1)[k]
d1 = dijkstra(k)[x]
result = d0 + d1
if result >= INF:
    print(-1)
else:
    print(result)