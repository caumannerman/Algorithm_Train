# 거슬러 줘야하는 동전 + 지폐 수 구하기! ( 지폐 단위가 서로 약,배수 관계가 아닌 경우)

#첫 째 줄에 거슬러줘야하는 금액을 입력받고,( 돈의 최소단위는 10원이다)
# 둘 째 줄에 ' '으로 구분하여 화폐 단위 액수를 입력.

n = int(input())
don = list(map(int, input().split()))

dpTable = [0]*(n//10 + 1)

for i in don:
    dpTable[i // 10] = 1

def dpJanDon(n):
   dpTable[n//10] = min( dpJanDon(n-x) for x in don if n-x >= 0)+1
   return dpTable[n//10]


dpJanDon(n)



print(dpTable[n//10])
print(dpTable)

