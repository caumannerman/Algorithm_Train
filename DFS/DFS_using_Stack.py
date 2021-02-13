graph = [[0,1,1,2,2,2,2,1], [1,0,2,2,2,2,1,2], [1,2,0,1,1,2,2,2], [2,2,1,0,1,2,2,2], [2,2,1,1,0,2,2,2], [2,2,2,2,2,0,1,2], [2,1,2,2,2,1,0,1], [1,2,2,2,2,2,1,0]]

visited = [False]*8



stack = [0]
visited[0] = True

def dfs(graph, visited, stack):
    v = stack[-1]

    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            stack.append(i)
            print(stack)
            visited[i] = True
            dfs(graph,visited, stack)

    stack.pop()
    print(stack)



dfs(graph, visited, stack)

