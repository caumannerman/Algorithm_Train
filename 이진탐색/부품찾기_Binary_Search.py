"""전자매장에 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 견적서를 요청했다.
이 떄, 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하자."""

# 첫 째 줄에서 N을 입력받고, 둘 째 줄에 N개의 정수를 공백으로 구분하여 입력받는다.
# 둘 째 줄에서 M을 입력받고, 둘 째 줄에서 M개의 정수를 공백으로 구분하여 입력받는다.

n = int(input())

mylist = list(map(int, input().split()))

m = int(input())

clist = list(map(int, input().split()))


'''풀이 1 : 라이브러리 이용 정렬 후, 이진탐색 '''


def bin_search(array, target, start, end):
    while True:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = start + 1

        if start > end:
            return None


mylist.sort()


for i in clist:
    if bin_search(mylist, i, 0, len(mylist)-1) == None:
        print('no', end = ' ')
    else:
        print('yes', end =' ')