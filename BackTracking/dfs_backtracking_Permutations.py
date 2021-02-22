n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
result = [0] * m
visited = [False] * n

def dfs(level):
    if level == len(result):
        print(*result)
        return

    for i in range(len(arr)):
        if not visited[i]:
            result[level] = arr[i]
            visited[i] = True
            dfs(level+1)
            visited[i] = False

dfs(0)