import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x,y)])
   # print("start : ", x, y)
    visited[x][y] = True
    idx = 0
    while len(q) > idx:
        for i in range(4):
            #print("nx, ny making....")
            nx = q[idx][0] + dx[i]
            ny = q[idx][1] + dy[i]
            #print("q[idx] = ", q[idx], "nx : ", nx, "ny : ", ny)
            if nx >= n or ny >= n or nx < 0 or ny < 0 :
                continue
            #print("data[nx][ny] = ", data[nx][ny], "data[x][y] = ", data[x][y])
            if not visited[nx][ny] and  l <= abs(data[nx][ny] - data[q[idx][0]][q[idx][1]]) <= r:
                q.append((nx,ny))

                #print(x,y, "appends", nx, ny)
                #print(q)
                visited[nx][ny] = True
        #print("end 4 iter")
        idx += 1
        #print("dix : ", idx)
    if len(q) > 1:
        temp = 0
        for (qx, qy) in q:
            temp += data[qx][qy]
        temp //= len(q)
        for (qx, qy) in q:
            data[qx][qy] = temp
        return True
    return False


result = 0
tick = False
while True:
    tick = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j):
                    tick = True
    if tick:
        result += 1
        #for i in data:
            #print(i)
        #print()
        continue
    break
print(result)