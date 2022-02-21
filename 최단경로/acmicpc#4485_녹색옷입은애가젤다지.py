""" DP로 풀어야하는 것인가 헷갈릴 수 있으나, DP로 풀이하기에는 삥~ 돌아가야하는 길을 처리할 수 없다
    이 문제는 DIjkstra로 풀이하는데, 일반적으로 인접 리스트로 주어지는 다익스트라 문제가 아니라
    인접행렬로 주어지는 그래프 상에서 풀이해야한다.
    데이터 걱정으로 2차원 Distance 행렬을 두지 않으려고 했으나, 생성하고 나니 매우 수월하게 풀이하였다."""

import sys
import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)
t = 0

def dijkstra(t, start_x, start_y):
    q = [(data[start_x][start_y], start_x, start_y)]
    distance[start_x][start_y] = data[start_x][start_y]
    while q:
        dist, now_x, now_y = heapq.heappop(q)
        if now_x == n - 1 and now_y == n - 1:
            print("Problem " + str(t) + ": " + str(dist))
            return
        if distance[now_x][now_y] < dist:
            continue
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + data[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
while True:
    t += 1
    n = int(input())
    if n == 0:
        exit()

    data = []
    distance = [[INF] * n for _ in range(n)]

    for _ in range(n):
        data.append(list(map(int, input().split())))
    result = 0
    dijkstra(t, 0, 0)
