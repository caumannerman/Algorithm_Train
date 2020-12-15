
'''비용 없는 인접 리스트 그래프용 DFS'''

# 노드 번호가 1번부터이므로, 복잡하지 않게 graph와 visited 리스트의 맨 앞은 비워두자


# 노드의 갯수 입력받음 
n = int(input())
# 노드의 갯수 + 1 개의 리스트를 원소로 가지는 리스트, 즉 2차원 배열을 생성 / n+1개인 이유는 노드 번호와 인덱스 번호를 맞춰주기 위
graph = [[] for _ in range(n+1)]
    
# 간선의 갯수도 입력받음

m = int(input())

# 이와 같이 비용이 없는 인접 리스트 그래프를 완성시킨다.

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
########################중요/  간선의 방향이 없기 때문에, 두 쪽 모두에 추가해 주어야 함

start = int(input())
visited = [False]*(n+1)
result = []

def dfs(graph, v, visited):
    result.append(v)
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



dfs(graph, start, visited)

print(result)
