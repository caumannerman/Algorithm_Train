"""당신은 화성 탐사 기계를 개발하는 프로그래머이다. 그런데 화성은 에너지 공급원을 찾기가 힙들다.
그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발지점에서 목표지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야한다.
화성탐사 기ㅖ가 존재하는 공간은 NxN 크기의 2차원공간이며, 각각의 칸을 지나기 위한 비용이 존재한다. 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래칸인
[N-1][N-1]위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하라.
화성탐사기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다."""
# 입력 : 첫 째 줄에 테스트 케이스의 수 T(1~10)이 주어진다.
# 매 테스트 케이스의 첫 째 줄에는 탐사공간의 크기를 의미하는 정수 N이 주어진다.(2~125)
# 이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분한다( 각칸의 비용 0~9)
# 출력 : 각 테스트 케이스마다 [0][0]의 위치에서 [N-1][N-1]의 위치로 이동하는 최소비용을 한 줄에 하나씩 출력한다.
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
t = int(input())
dx = [-1, 0,1,0]
dy = [0, 1, 0, -1]
INF = int(1e9)


for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    q = [(distance[0][0], 0, 0)]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))

    print(distance[n-1][n-1])

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4



출력 20 19 36'''