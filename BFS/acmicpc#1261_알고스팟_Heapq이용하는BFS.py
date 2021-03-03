"""알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다.
미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다.
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때,
이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.
벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.
만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만,
안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.
현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다.
# 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.
# (1, 1)과 (N, M)은 항상 뚫려있다.
# 출력 : 첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.


'''맨 처음에는 heapq가 아닌, bfs에서 항상 사용하는 deque를 사용하였다. 그러고 보니,visited를 사용하는 의미가 없었다. 만약, 삥삥 돌면, 벽을 하나도 뚫지 않고 n-1,m-1에 도달할 수 있는
길이 존재한다면, 답은 0이 나와야한다. 그런데, 벽을 뚫고 지나간 경로가 먼저 0을 지나가, deque에 들어가게 되면, 삥삥 돌아 벽을 안 뚫고 도착할 수 있는 경로의 0의 visited를 1로 만들어,막아버리는 경우가 생긴다는 것.
 
visited를 쓰지 않고, 큐를 계속 돌려, n-1,m-1에 도달하는 경로들을 모두 모아, 각 경로들이 벽을 뚫은 횟수 중 최솟값을 가져올 수 있겠지만, 계산이 4의 거듭제곱으로 계속 쌓여 무조건 시간초과.

이는 다익스트라와 같이  heapq를 사용하면 해결되었다.

결론적으로, 우리는 벽을 뚫지 않고 가는 경로 --> 벽을 1 번 뚫고 가는 경로, --> 벽을 2번 --> 3번  ... 순으로 체크를 해주는 것이 가장 좋다.
이 기능ㅇ르 heapq가 해주는 것.

'''
import sys
import heapq
input = sys.stdin.readline
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False]* m for _ in range(n)]



def bfs(x, y):
    q = [(0,x,y)]
    visited[x][y] = 1

    while q:
        bkhs, now_x, now_y = heapq.heappop(q)
        if now_x == n - 1 and now_y == m - 1:
            return bkhs
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    heapq.heappush(q, (bkhs, nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 1:
                    heapq.heappush(q, ( bkhs+1, nx, ny))
                    visited[nx][ny] = True


print(bfs(0,0))
