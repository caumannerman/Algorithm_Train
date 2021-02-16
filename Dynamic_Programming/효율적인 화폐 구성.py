"""N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 이 때 각 화폐는 몇개라도 사용할 수 있으며, 사용한
화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐개수이다."""
# 입력 : 첫 째 줄에 N,M이 주어진다. ( 1<=N <= 100, 1<=M <= 10,000 )
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.
# 출력 : 첫 째 줄에 M원을 만들기 위한 최소한의 화폐개수를 출력한다.
# 불가능 할 때는 -1을 출력한다.

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

dp = [0] * (m+1)
for i in data:
    if i <= m:
        dp[i] = 1

for i in range(2,m+1):
    if dp[i] != 0:
        continue
    tmp = []
    for j in data:
        if i - j > 0:
            if dp[i-j] != 0:
                tmp.append(dp[i-j] + 1)
    if not tmp:
        continue
    dp[i] = min(tmp)

if dp[m] == 0:
    print(-1)
else:
    print(dp[m])