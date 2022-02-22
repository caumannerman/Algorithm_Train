import sys

input = sys.stdin.readline
n = int(input())

data = [True] * (n + 1)

for i in range(2, int( n ** 0.5) + 1):
    if data[i]:
        for j in range(i + i, n + 1, i):
            data[j] = False

prime = [i for i in range(2, n + 1) if data[i]]

end = 0
summary = 0
count = 0
numOfPrime = len(prime)

for start in range(numOfPrime):
    while summary < n and end < numOfPrime:
        summary += prime[end]
        end += 1

    if summary == n:
        count += 1
    summary -= prime[start]
print(count)