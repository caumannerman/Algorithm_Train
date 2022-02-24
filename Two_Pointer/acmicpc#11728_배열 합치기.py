import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
pa = 0
pb = 0

while pa < n and pb < m:
    if a[pa] < b[pb]:
        result.append(a[pa])
        pa += 1
    else:
        result.append(b[pb])
        pb += 1

if pa < n:
    result.extend(a[pa:])
else:
    result.extend(b[pb:])

print(*result)

