"""방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다.
# (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
# a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다.
# (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
# 출력 : 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
g1,g2 = map(int ,input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q = [(0,start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
""" 여기서 g1 == 1일 때, g2 == n일때, 그리고 둘 모두일 때, 모두 아닐때 총 4가지 경우를 나눠 조건문을 사용해 dijkstra함수 호출 횟수를 줄일 수 있는 경우에는 줄여보았지만,
별 차이 없다! ==> 그냥 코드 빠르게 짜는게 낫다. d1,dg2, dg1 세번의 dijkstra함수 호출마다 distance를 함수 내부에서 생성하여 리턴해주는 것이 포인트@@"""

''' 다익스트라 함수가 돌아가는 과정에서, 큐에 들어가는 튜플의 원소 수를 (거리, 노드번호, 지나야할 노드를 지났으면 1 아니면 0)과 같이 하나 늘려서 효율적으로 찾아볼까 했지만
...'''
d1 = dijkstra(1)
dg1 = dijkstra(g1)
dg2 = dijkstra(g2)
result = min(d1[g1] + dg1[g2] + dg2[n], d1[g2] + dg2[g1] + dg1[n])
if result >= INF:
    print(-1)
else:
    print(result)