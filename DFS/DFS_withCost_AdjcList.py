
'''DFS with 경로마다 비용이 존재하는 그래프 (인접 리스트)'''

graph = [ [], [(2,5), (3,9), (8,4)], [(1, 5), (7,7)], [(1,9), (4,2)], [(3,2),(5,3)], [(3,1), (4,3)], [(7,2)], [(2,7), (6,2), (8,6)], [(1,4), (7,6)]]

visited = [False]*9

stack = []
total_Cost = 0

def dfs(graph, visited, vertex):
    visited[vertex] = True
    stack.append(vertex)

    for i in graph[vertex]:
        if visited[i[0]] == False:
            dfs(graph, visited, i[0])

