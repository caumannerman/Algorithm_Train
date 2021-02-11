"""정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력시, 00:00:03     00:13:30 등 모두 포함해야한다."""


n = int(input())

x = 0
if 3<=n and n < 13:
    x = 1
elif 13<= n and n < 23:
    x = 2
else:
    x = 3

print((3600 - 45 ** 2) * (n+1) + (45 ** 2) * x  )


# 풀이2
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)
