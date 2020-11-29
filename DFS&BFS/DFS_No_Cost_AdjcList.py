
'''비용 없는 인접 리스트 그래프용 DFS'''

# 노드 번호가 1번부터이므로, 복잡하지 않게 graph와 visited 리스트의 맨 앞은 비워두자
graph = [ [], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]

visited = [False]*9

stack = list()

def dfs(graph, visited, vertex):

    visited[vertex] = True
    stack.append(vertex)
    print(stack)

    for i in graph[vertex]:
        if not visited[i]:

            dfs(graph, visited, i)

    stack.pop()
    print(stack)


dfs(graph,visited,1)