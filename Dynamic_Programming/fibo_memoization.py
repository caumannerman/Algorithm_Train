memo = [0]*100

# 1. 메모이제이션이므로 dp테이블 생성
# 2. 기초값  리턴값 지정
# 3. 기초값 아닌경우 , 계산한 적 있는지 확인
# 4. 계산한 적 없다면, 계산해서 저장하고 리턴!

def fibo(n):

    if n == 1 or n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(10))
