"""n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다."""
# 입력 : 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다.
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
# 출력 : 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
#
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.
#
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.


"""역추적하는 방법에 두가지가 있다. distance 배열을 2차원으로 만들어, 1번인덱스에 해당 노드까지 최단거리 경로를 갱신
 
      2. distance배열은 기본 Dijkstra와 동일하게 두고, before 배열을 (n+1) 크기로 생성하여, dijkstra함수 안에서 갱신이 될 때마다, 
         before[new] = now 로 갱신해준다.  즉, 각 노드마다, 최단거리로 도달할 때, 거쳐야하는 "직전노드"를 before 배열에 저장하는 것."""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
distance = [[INF,""] for _ in range(n+1)]


def dijkstra(start):
    distance[start][0] = 0
    distance[start][1] = str(start)
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now][0] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]][0] > cost:
                distance[i[0]][0] = cost
                distance[i[0]][1] = distance[now][1] +"," + str(i[0])
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance[end][0])
trace = distance[end][1].strip().split(",")
print(len(trace))
print(*trace)