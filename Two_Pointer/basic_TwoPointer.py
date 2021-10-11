import sys
input = sys.stdin.readline

# data갯수, 찾고자하는 부분합 s
n, s = map(int, input().split())
data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for start in range(0,n):
    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == s:
        count += 1
    interval_sum -= data[start]

print(count)