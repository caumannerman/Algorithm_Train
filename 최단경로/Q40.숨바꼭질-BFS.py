""" 간선에 비중이 있는경우에는 BFS로 풀이를 할 수 없다.
BFS는 덱을 사용하는데, 각 노드까지 걸리는 이동 횟수를 알 수 있지만, 그 간선들에 비중이 있다면, 그를 지속적으로 계산하고, 각 순간까지 남은 최소거리 노드를 알려주는
(heapq를 사용할 때의 min_node()함수 )를  또 따로 처리해줘야 가능하다.
따라서 비중이 있는 경우에는 heapq를 사용하는 Dijkstra를 사용해야한다.

사실 두가지 알고리즘은 덱을 사용하냐, 우선순위 큐를 사용하냐의 차이지 비슷한 모양을 띤다.
BFS는 graph와  visited(distance의 역할도 함께 해줌), 그리고 bfs함수에서 q 와 while q:

Dijkstra는 graph와 distance,  그리고 dijkstra 함수에서의 q(heapq)와 while q:

또한, 둘 다 start지점을 매개변수로 받아, 그 지점으로부터 다른 모든 지점까지의 최단거리를 알 수 있다.

따라서

간선에 비용이 없으면 BFS, 비용이 없으면 Dijkstra를 사용하자!!!!!!!!!!!!!!!!

"""
from collections import deque
import sys
input = sys.stdin.readline
n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def bfs(start):
    minmax_idx = -1
    max_dist = 0
    max_count = 0
    visited[start] = 1

    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                if max_dist < visited[i]:
                    max_dist = visited[i]
                    max_count = 1
                    minmax_idx = i
                elif max_dist == visited[i]:
                    max_count += 1
                    minmax_idx = min(minmax_idx, i)
                q.append(i)
    return minmax_idx, max_dist-1, max_count

s = bfs(1)
print(*s)
