""" 주인공이 N x M 크기의 직사각형 형태의 미로에 갇혀있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다.
주인공의 위치는 (1,1)이고, 미로의 출구는 (N,M)의 위치에 존재하며, 한번에 한 칸씩 이동할 수 있다.
이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이 때, 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 갯수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
"""
# 첫 줄에 두 정수 n,m이 주어진다. (4<=n, m<= 200)
# 다음 n개 줄에는 각각 m개의 정수(0혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백없이 붙어서 입력된다. 시작 칸, 마지막 칸은 항상 1이다.
# 출력 - 첫 줄에 최소 이동칸의 갯수 출력
from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))



dx = [1,0,-1,0]
dy = [0,1,0,-1]


q = deque([(0,0)])

while q:
    now_x, now_y = q.popleft()

    for i in range(4):
        if now_x+dx[i] >= 0 and now_x+dx[i] < n and now_y+dy[i] >= 0 and now_y + dy[i] < m:
            if now_x+dx[i] == n-1 and now_y + dy[i] == m-1:
                print(graph[now_x][now_y] + 1)
                quit()
            if graph[now_x+dx[i]][now_y+dy[i]] == 1:
                graph[now_x + dx[i]][now_y + dy[i]] = graph[now_x][now_y] + 1
                q.append((now_x + dx[i],now_y + dy[i]))




