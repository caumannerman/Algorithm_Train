
# 앞선 Memoization방식은 Top-Down방식이다. ( 큰 문제 해결 위해 작은 문제를 호출하므로 )
# 단순 반복문 이용하여 소스코드를 작성하는 경우는 Bottom-Up 방식이라고 함.
"""Bottom-Up 방식이 다이나믹 프로그래밍의 전형적 형태이다. """
d = [0]*100

d[1], d[2] = 1, 1
n = int(input("피보나치 수열의 몇 번 째 숫자를 계산하시겠습니까? : "))

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])