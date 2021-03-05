import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
before = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
distance[s] = 0

q = []
heapq.heappush(q, (0, s))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = i[1] + dist
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            before[i[0]] = now
            heapq.heappush(q, (cost, i[0]))

print(distance[e])

path = []
tmp = e
# 이 곳을 path.append(before[tmp]) 이런식으로 하면 메모리 초과!
while tmp != 0:
    path.append(tmp)
    tmp = before[tmp]

print(len(path))
print(*path[::-1])