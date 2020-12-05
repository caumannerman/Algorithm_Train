'''정수 X가 주어질 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
       1. X가 5로 나누어떨어지면, 5로 나눈다.
       2. X가 3으로 나누어떨어지면, 3으로 나눈다.
       3. X가 2로 나누어떨어지면, 2로 나눈다.
       4. X에서 1을 뺀다.

       정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.'''


'''  처음 작성했던 코드 - 폐기처분
# 점화식으로 나타내면, An = min(A(n-1), A(n/2), A(n/3), A(n/5)) + 1
dp = [0]*300001

n = int(input())

array = [2,3,5]

for i in range(2, n+1):
    temp = []
    for j in array:
        if i % j == 0:
            temp.append(i//j)
    if not temp:
        dp[i] = dp[i-1] + 1
    else:
        for k in range(len(temp)):
            temp[k] = dp[temp[k]]
            temp.append(dp[i-1])
        print(temp)
        dp[i] = min(temp) + 1


print(dp[n])
'''
# 12.5 새롭게 작성한 코드 ( 훨씬 가독성 좋고 짧음 )
dp = [0]*30001
dp[2], dp[3], dp[5] = 1, 1, 1

n = int(input())
tmp = (2,3,5)

for i in range(4,n+1):
    arr = [dp[i-1]]
    for k in tmp:
        if i%k == 0:
            arr.append(dp[i//k])
    dp[i] = min(arr) + 1

print(dp[n])