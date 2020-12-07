#12.7 Dijkstra
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


#------------------------------- 여기까지가 기본 세팅 ----------------------------------------------

def min_index():
    min_d = INF
    min_i = -1
    for i in range(len(distance)):
        if distance[i] < min_d:
            if not visited[i]:
                min_d = distance[i]
                min_i = i
    return min_i


def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    nv = start
    while True:
        for i in graph[nv]:
            distance[i[0]] = min(distance[i[0]], distance[nv] + i[1])
        nv = min_index()
        visited[nv] = True
        if visited[1:] == [True]*n:
            break

dijkstra(start)

print(distance)

'''

# 12.7 Improved Dijkstra

# 이 코드의 차별점은, 최소 비용 노드를 뽑아주는 함수를 작성하지 않아도 되는 것과, heapq를 이용한 우선순위 큐를 이용하는 것.
# 최소비용 노드를 뽑아주는 연산의 시간복잡도가 기존에는 O(N)였지만, O(logN)으로 가능하게 된다.
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
# heapq를 사용할 것이기 때문에 (c,b)로 비용을 앞에 오게 하여 추가하는 것임

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:

        dis, v = heapq.heappop(q)
        if distance[v] < dis:
            continue

        for i in graph[v]:
            if distance[v] + i[0] < distance[i[1]]:
                distance[i[1]] =  distance[v] + i[0]
                heapq.heappush(q, (distance[i[1]], i[1]))

dijkstra(start)

print(distance)
'''

#12.8 Floyd-Warshall Algorithm

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i:
            continue
        for k in range(1, n+1):
            if k == i or k == j:
                continue
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]


print(graph)