import sys
input = sys.stdin.readline

n, m = map(int, input().split())
setdata = []
onedata = []
for _ in range(m):
    a, b = map(int, input().split())
    setdata.append(a)
    onedata.append(b)
smin = min(setdata)
smin_1 = smin / 6
omin = min(onedata)

if smin_1 >= omin:
    print(n * omin)
else:
    print(min((n // 6) * smin + (n % 6) * omin, ((n // 6) + 1) * smin))
