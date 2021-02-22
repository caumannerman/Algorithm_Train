n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
result = [0] * m



def dfs(level,begin, n, m):
    if level == m:
        print(result)
        return
    for i in range(begin,n):
        result[level] = arr[i]
        dfs(level + 1, i + 1, n, m)


dfs(0,0,n,m)