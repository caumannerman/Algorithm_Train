"""BFS는 너비우선 탐색  Breadth First Search"""
''' 일반적으로 실제 수행시간이 DFS보다 좋은 편이라고 한다.. 시간복잡도는 O(N)'''
#  1. 탐색시작노드를 큐에 삽입 + 방문처리
   # 2. 큐에서 하나를 꺼내, 해당 노드의 인접 노드 중에서 방문X 노드를 모두 큐에 삽입 + 방문처리
   # 3. 2번을 수행할 수 없을 때까지 반복

"""
visited = [False]*9

queue = deque([])

def bfs( graph, visited, vertex):
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



bfs(graph, visited, 1)
"""

from collections import deque

# 노드,간선  갯수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

#간선 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = int(input())
visited = [False]*(n+1)

def bfs(graph, start, visited):
    q = deque([])
    visited[start] = True
    q.append(start)
    print([q[0]])
    while q:
        now = q.popleft()
        temp = []
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                temp.append(i)
        print(temp)



bfs(graph, start, visited)



