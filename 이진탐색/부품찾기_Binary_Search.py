"""전자매장에 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 견적서를 요청했다.
이 떄, 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하자."""

# 첫 째 줄에서 N을 입력받고, 둘 째 줄에 N개의 정수를 공백으로 구분하여 입력받는다.
# 셋 째 줄에서 M을 입력받고,  넷 째 줄에서 M개의 정수를 공백으로 구분하여 입력받는다.

n = int(input())
my = list(map(int, input().split()))
m = int(input())
client = list(map(int, input().split()))


def bin_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start+end) //2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bin_search(arr, target, start, mid-1)
    else:
        return bin_search(arr, target, mid+1, end)

for i in client:
    if bin_search(my,i,0,n-1) != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')



