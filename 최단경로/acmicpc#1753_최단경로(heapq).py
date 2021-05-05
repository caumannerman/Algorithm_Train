"""방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다."""
# 출력 : 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

import heapq
import sys
""" 두 정점 사이에 여러 개의 간선이 존재할 수 있지만 그에 대해서는 별다른 조치를 취하지 않아도 된다.
 a 노드에서 어떤 다른 b라는 노드로의 길이 두가지 존재한다고 하자. 
 b로의 두가지 길 중, 큰 비용을 가지는 경로는 필요가 없다. 하지만, 우리가 for문 내에서 큰 비용 경로를 먼저 체크하고, 갱신되어, distance에 들어갔다고 하더라도,
 해당 for문 내에서 더 적은 비용의 경로로 갱신된다.
 적은 비용 경로로 먼저 갱신되었을 경우, 해당 for문에서 큰 비용의 경로를 체크할 때는 무시하고 지나가게 된다."""
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    q.append((0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)