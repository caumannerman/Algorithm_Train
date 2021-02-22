n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
result = []

def dfs(count):
    if count == m:
        print(result)
        return
    for i in range(len(arr)):
        result.append(arr[i])
        dfs(count + 1)
        result.pop()

dfs(0)
