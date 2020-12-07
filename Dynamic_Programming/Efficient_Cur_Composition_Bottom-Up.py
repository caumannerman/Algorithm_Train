""" N가지 종류 화폐가 있다. 이 화폐들의 개수를 최고한으로 이용하여, 그 가치의 합이 M원이 되도록 하려 한다. 이때 각 화폐는 몇개라도 사용할 수 있으며,
사용한 화폐 구성은 같지만 순서만 다른것은 같은 경우로 생각한다.  예를들어 2,3원 단위의 화폐가 있을 때, 15원을 만들기 위해   3원을 5개 사용하는 것이 최소한의 개수이다."""

# 첫 째 줄에 N, M이 주어진다. ( N은 1~100사이 M은 1~10000사이 )
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

# 첫 쨰 줄에는 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# 불가능할 때는 -1을 출력한다.

n, m = map(int, input().split())

cur = []
for i in range(n):
    cur.append(int(input()))

d = [10001]*(m+1)

d[0] = 0

for i in range(n):
    for j in range(cur[i], m+1):
        if d[j- cur[i]] != 10001:
            d[j] = min(d[j], d[j - cur[i]] + 1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])