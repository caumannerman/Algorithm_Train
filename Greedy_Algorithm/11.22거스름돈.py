'''첫 째 줄에 거슬러줘야할 돈의 액수를 입력받고, 둘 째 줄에 화폐 단위를 ' '으로 구분하여 입력받는다. 거슬러줘야할 동전의 최소갯수를 구하는 문제'''


import timeit
# 그리디 알고리즘은 "정당성"을 항상 체크해줘야 한다.
n = int(input())

start = timeit.default_timer()

count = 0

'''  동전의 종류가 많아지면 주석 안의 내용처럼, 동전의 종류를 list에 넣고, 반복문으로 처리하는게 훨씬 좋
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
'''
if n >= 500:
     count += n // 500
     n %= 500

if n >= 100:
    count += n // 100
    n %= 100

if n >= 50:
    count += n // 50
    n %= 50

if n >= 10:
    count += n // 10   # 마지막에는 n을 굳이 수정하지 않아도 됨.

print("거슬러줘야할 동전의 갯수는 ", count, "입니다.")

stop = timeit.default_timer()

print(stop-start)

# 지금과 같이 동전의 종류 수가 4개로 적을 때는, 동전 갯수만큼의 if문을 통해 동전의 갯수를 구해주는 것이 더 빠르거나 비슷비슷한 것 같다.
# 하지만 동전의 종류가 매우 많아지면, 숫자만 다른  똑같은 내용의 조건문을 일일이 다 써주기보다는, 반복문과 list(동전 종류를 포함하고있는)로 코드 작성!