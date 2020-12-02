'''최단 경로 알고리즘 ( 다익스트라, 플로이드 워셜, 벨만포드) 이 3가지 알고리즘으로 대표됨  '''

'''dijkstra 최단경로 알고리즘은, 그래프에서 여러 노드가 있을 때, 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
       (음의 간선이 없어야함)    다익스트라 알고리즘은 실제 GPS SW의 기본 알고리즘'''
# 다익스트라는 Greedy Algorithm의 일종 ( 매번 가장 비용이 적은 노드를 선택 )

'''다익스트라 과정 
       1. 출발노드 설정
       2. 최단 거리 테이블 초기화
       3. 방문하지 않은 노드 중, 최단거리가 가장 짧은 노드 선택
       4. 해당 노드 거쳐 다른노드로 가는 비용 계산하여 최단거리 테이블 갱신
       5. 3,4번을 반복 '''

import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수와 간선의 수 입력받음
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

#그래프 정보 받아서 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def min_distance_node():
    min_d = INF
    min_v = 0
    for i in range(1, n+1):
        if visited[i] == False and distance[i] < min_d:
            min_d = distance[i]
            min_v = i
    return min_v

def dijkstra(v):
    distance[v] = 0
    visited[v] = True

    for i in graph[v]:
        distance[i[0]] = i[1]

    while True:
        nv = min_distance_node()
        visited[nv] = True

        if visited[1:] == [True]*n:
            break

        for k in graph[nv]:
            distance[k[0]] = min(distance[k[0]], k[1] + distance[nv])


dijkstra(start)


for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
