n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
result = []

def dfs(idx, count):
    if count == m:
        print(*result)
        return
    for i in range(idx, len(arr)):
        result.append(arr[i])
        dfs(i, count + 1)
        result.pop()