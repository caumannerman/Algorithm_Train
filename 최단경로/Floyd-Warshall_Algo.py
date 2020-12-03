''' 플로이드 워셜 알고리즘은 " 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우" 에 사용한다.'''
# 플로이드 워셜 알고리즘은 다이나믹프로그래밍
# 노드 N개일 때, N번의 단계를 반복하며, 점화식에 맞게 2차원리스트를 갱신함.
#3중 반복문
""" 플로이드 워셜 알고리즘의 점화식 :    Dab = min( Dab, Dak + Dkb )"""

"""과정"""
# 1. n x n크기의 2차원 배열에서 대각선은 모두 0 으로( 자기 자신으로의 비용이므로) 채우고, 간선이 존재하는 곳은 간선 비용 그대로, 연결이 없는 경로에 대해서는 INF(1e9)로 채운다.
# 2. 1번 노드를 거쳐가는 경우를 고려한다. 총 고려해야할 경우의 수는 n-1P2 이다(Permutation)
# 더 작은 값이 나오면 테이블을 갱신해준다.



INF = int(1e9)
#노드 갯수 n, 간선 갯수 m
n ,m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

# 그래프 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i:
            continue
        for k in range(1, n+1):
            if k == i or k == j:
                continue
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
            if graph[k][j] > graph[k][i] + graph[i][j]:
                graph[k][j] = graph[k][i] + graph[i][j]

for i in graph[1:]:
    print(i[1:])


'''간단하게
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 이렇게만 해도 플-워-알고리즘 완성 '''
