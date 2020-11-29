from collections import deque

# 노드 번호는 0번부터 시작한다고 하자.
# 연결이 되어있는 관계는 1, 연결이 없는 관계는 편의상 2로, 자기자신에는 0으로 표기하였다.


# 여러모로 비용이 없는 그래프의 경우에는 인접 리스트가 효율적이다! ( 인접한지 한 번 더 체크해주지 않아도 됨 )

graph = [[0,1,1,2,2,2,2,1], [1,0,2,2,2,2,1,2], [1,2,0,1,1,2,2,2], [2,2,1,0,1,2,2,2], [2,2,1,1,0,2,2,2], [2,2,2,2,2,0,2,1], [2,1,2,2,2,1,0,1], [1,2,2,2,2,2,1,0]]

visit = [False]*8

queue = deque([])

def bfs(graph, visited, start):

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)



bfs(graph, visit, 0)