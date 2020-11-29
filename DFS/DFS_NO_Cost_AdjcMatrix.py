'''비용이 없는 그래프를 인접행렬로 나타낸 자료를 이용한 DFS '''
# 노드 번호는 0번부터 시작한다고 하자.
# 연결이 되어있는 관계는 1, 연결이 없는 관계는 편의상 2로, 자기자신에는 0으로 표기하였다.


# 여러모로 비용이 없는 그래프의 경우에는 인접 리스트가 효율적이다! ( 인접한지 한 번 더 체크해주지 않아도 됨 )
graph = [[0,1,1,2,2,2,2,1], [1,0,2,2,2,2,1,2], [1,2,0,1,1,2,2,2], [2,2,1,0,1,2,2,2], [2,2,1,1,0,2,2,2], [2,2,2,2,2,0,2,1], [2,1,2,2,2,1,0,1], [1,2,2,2,2,2,1,0]]

visited = [False]*8

stack =list()

def dfs(graph, visited, vertex):
    visited[vertex] = True
    stack.append(vertex)
    print(stack)

    for i in range(len(graph[vertex])):  # 비용 없는 인접리스트에서는 리스트에 있다는 자체가 인접함을 나타내는데, 인접 행렬에서는 인접한 것을 체크해줘야하므로, 한 번의 체크가 더 필요하다...
        if graph[vertex][i] == 1 and visited[i] == False:
            dfs(graph, visited, i)

    stack.pop()
    print(stack)

dfs(graph, visited, 0)