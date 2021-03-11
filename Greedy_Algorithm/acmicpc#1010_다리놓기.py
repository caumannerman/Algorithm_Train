t = int(input())
def fact(n):
    result = 1
    while n >1:
        result *= n
        n -= 1
    return result
for _ in range(t):
    a, b = map(int, input().split())
    tmp = a
    result = 1
    while a>0:
        result *= b
        a -= 1
        b -= 1
    result //= fact(tmp)
    print(result)