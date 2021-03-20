n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
result = [0] * m

# 조합이므로, 순열과는 다르게, 순서만 다른 경우는 모두 같은 경우가 되는 것이다. 이 기준을 begin 매개변수를 이용해 충족시켜주고있는데,
# 기본적으로 arr배열에 있는 것들을 앞에서부터 차례로 뽑아 그 순서 그대로 가져가는 것이 코드에 반영되어있다.
# 백트래킹 Permutation과 같이 visited를 하지 않아도 되는 이유는, result에 그냥 매번 새로 덮어씌우면 되기도 하고,
# 가장 큰 이유는 순서를 arr에 저장되어있는 그대로 가져오는 것이 규칙이기 때문에, visited가 없어도 되는 것.

def dfs(level,begin, n, m):
    if level == m:
        print(*result)
        return
    for i in range(begin,n):
        result[level] = arr[i]
        dfs(level + 1, i + 1, n, m)

# arr = [1,2,3,4,5]이면, arr[0] = 1이 되고나서, 그 뒤쪽이 재귀에 의해 모두 진행된 후,
# arr[0] = 1인 경우가 또 시작되어 모두 처리.
# arr[0] = 2인 경우 ~~ arr[0] = 3 , arr[0] = 4, arr[0] = 5까지 차례로 모두 실행되는 것.
dfs(0,0,n,m)