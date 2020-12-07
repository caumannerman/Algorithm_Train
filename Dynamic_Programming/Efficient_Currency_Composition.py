""" N가지 종류 화폐가 있다. 이 화폐들의 개수를 최고한으로 이용하여, 그 가치의 합이 M원이 되도록 하려 한다. 이때 각 화폐는 몇개라도 사용할 수 있으며,
사용한 화폐 구성은 같지만 순서만 다른것은 같은 경우로 생각한다.  예를들어 2,3원 단위의 화폐가 있을 때, 15원을 만들기 위해   3원을 5개 사용하는 것이 최소한의 개수이다."""

# 첫 째 줄에 N, M이 주어진다. ( N은 1~100사이 M은 1~10000사이 )
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

# 첫 쨰 줄에는 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# 불가능할 때는 -1을 출력한다.

# Top-Down
n, m = map(int, input().split())
cur = []

for _ in range(n):
    cur.append(int(input()))

cur.sort()

dp = [0]*(m+1)

for i in range(cur[0]):
    dp[i] = -10001

for i in cur:
    if i <= m:
        dp[i] = 1

def ecc(m):
    if dp[m] != 0:
        return dp[m]

    temp = [ecc(m-i) for i in cur if m-i >= 0 and ecc(m-i) > 0]

    if temp:
        dp[m] = min(temp) + 1
        return dp[m]

    dp[m] = -10000
    return dp[m]

if ecc(m) > 0:
    print(ecc(m))
else:
    print(-1)








