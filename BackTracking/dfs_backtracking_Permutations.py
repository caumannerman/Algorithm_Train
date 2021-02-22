n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
result = [0] * m
checked = [False] * n

def dfs(level,n,m):
    if level == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        if checked[i] == True:
            continue

        result[level] = arr[i]
        checked[i] = True
        dfs(level+1,n,m)
        checked[i] = False

dfs(0,n,m)