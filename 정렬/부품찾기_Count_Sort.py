"""전자매장에 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 견적서를 요청했다.
이 떄, 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하자."""

# 첫 째 줄에서 N을 입력받고, 둘 째 줄에 N개의 정수를 공백으로 구분하여 입력받는다.
# 둘 째 줄에서 M을 입력받고, 둘 째 줄에서 M개의 정수를 공백으로 구분하여 입력받는다.

n = int(input())

mylist = list(map(int, input().split()))

m = int(input())

client_list = list(map(int, input().split()))


countlist = [0]*1000001

for i in mylist:
    countlist[i] += 1

for j in client_list:
    if countlist[j] == 0:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

