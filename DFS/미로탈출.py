
'''

def dfs(x, y, graph, count):
    if graph[x][y] == 0 or graph[x][y] == 2 or x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return
    elif x == n - 1 and y == m - 1:
        result.append(count + 1)
    else:

        graph[x][y] = 2
        dfs(x + 1, y, graph, count + 1)
        dfs(x - 1, y, graph, count + 1)
        dfs(x, y + 1, graph, count + 1)
        dfs(x, y - 1, graph, count + 1)



n, m = map(int, input().split())  # 그래프가 n줄, 가로 m 이므로 탈출구는 n-1.m-1이다.

result = []

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))





dfs(0, 0, graph, 1)

result.sort()
print(result[len(result)-1])

'''
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

