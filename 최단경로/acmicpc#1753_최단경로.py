"""방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다."""
# 입력 : 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
# 출력 : 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

''' 틀렸던 이유 : dijkstra 함수 시작부분에서 distance[start]를 0으로, visited[start]를 True로 , 그리고 graph[start]에 있는 것들에 대하여
먼저 처리( distance리스트 값 ) 해주고  for문을 v-1번만큼 돌렸는데, 그렇게 하면 
start 지점에서 어떤 노드 x로의 간선이 두개 이상이고, 거리가 3,5 와 같이 오름차순인 경우, 3이 아닌 5가 distance[x]에 저장이 될 수 있으므로, 틀린 풀이였다.'''

import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int ,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [INF]*(v+1)
for _ in range(e):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))

def min_dist():
    min_distance = INF
    idx = 0
    for i in range(1,v+1):
        if distance[i] < min_distance and not visited[i]:
            min_distance = distance[i]
            idx = i
    return idx
def dijkstra(start):
    distance[start] = 0
    for i in range(v):
        now = min_dist()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
dijkstra(start)
for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)