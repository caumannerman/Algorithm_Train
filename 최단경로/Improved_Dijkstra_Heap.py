import heapq
import sys
input = sys.stdin.readline
# heapq의 메서드들   heapq.heappush
# heap.heappop
# heap.heapify(list)
INF = int(1e9)
# 노드의 수와 간선의 수 입력받
n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
# visited 리스트를 만들지 않고 heappop하여 나온 비용과 해당 노드의 distance에서의 값을 비교하여, visited여부를 체크해줄 수 있다. 노드 수가 많다면, visited 리스트를 줄이는 것이 작지만은 않을 듯.
visited = [False]*(n+1)
distance = [INF]*(n+1)

# a에서 b로 가는 비용이 c라는 의미. (b,c)를 튜플로 리스트에 추가함
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
# 여기서 미리 visited[start] = True 해주면 안됨!! -> while문에 들어가자마자 continue로 인해 돌아가고 힙이 비어서 끝남.
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        cost, nv = heapq.heappop(q)
        if visited[nv]:
            continue
        visited[nv] = True

        for i in graph[nv]:
            if i[1] + distance[nv] < distance[i[0]]:
                distance[i[0]] =  i[1] + distance[nv]
                heapq.heappush(q, (i[1] + distance[nv], i[0]))


dijkstra(1)

print(distance)