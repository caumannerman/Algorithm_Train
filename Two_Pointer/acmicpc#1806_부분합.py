import sys
input = sys.stdin.readline

n ,s = map(int, input().split())
data = list(map(int, input().split()))

end = 0
summary = 0
length = int(1e9)

for start in range(n):
    while summary < s and end < n:
        summary += data[end]
        end += 1
    if summary >= s:
        length = min( length, end - start)
    summary -= data[start]

if length == int(1e9):
    print(0)
else:
    print(length)