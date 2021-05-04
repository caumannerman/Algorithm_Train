"""어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다. 하지만 X라는 도시에서 Y라는 도시로 전보를 보내려한다면,
도시 X에서 Y로 향하는 통로가 설치되어있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면, Y는 X로 메시지를 보낼 수 없다.
또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다. 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개이며, 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오."""

# 첫 째 줄에 도시개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다. ( N 1~30,000   M은 1~200,000   c는 1~N )

# 둘 째 줄부터 M+1번 째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다. 이는 특정 도시 X에서 다른 특정도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미이다.

# 메시지를 받는 도시의 총 개수, 총 걸리는 시간을 공백으로 구분하여 출력.
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, c = map(int, input().split())
distance = [INF]*(n+1)

graph = [[] for _ in range(n+1)]


for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z,y))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, nv = heapq.heappop(q)
        for i in graph[nv]:
            if distance[i[1]] > distance[nv] + i[0]:
                distance[i[1]] = distance[nv] + i[0]
                heapq.heappush(q,(distance[i[1]], i[1]))

dijkstra(c)
count = 0
max_time = 0
for i in range(1,n+1):
    if distance[i] != INF and  i != c:
        count += 1
        max_time = max(max_time, distance[i])
print(count, max_time)
''' 이와 같이 수행하는 것이 오히려 빠르다. count를 그냥 1씩 더하고, 마지막에 count-1을 출력해주는 것.
for i in distance[1:]:
    if i != INF:
        count += 1
        max_time = max(max_time, i)

print(count-1, max_time)
'''