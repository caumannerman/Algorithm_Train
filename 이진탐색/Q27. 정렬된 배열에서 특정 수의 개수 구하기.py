"""N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이 때 이 수열에서 x가 등장하는 횟수를 계산하라. 예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때,
x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
  단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받는다. """

# 첫 째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다.
# 둘 째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다.
# 출력 - 수열의 원소 중에서 값이 x인 원소의 개수를 출력한다. 단, 값이 x인 원소가 하나도 없다면, -1을 출력한다.
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
data = list(map(int, input().rstrip().split()))

def left_bs(data, target,start, end):
    last = -1
    while True:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            last = mid
            end = mid - 1
        if start > end:
            break
    return last

def right_bs(data, target, start, end):
    last = -1
    while True:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            last = mid
            start = mid + 1
        if start > end:
            break
    return last

a = left_bs(data, m, 0, len(data)-1)
b = right_bs(data, m, 0, len(data)-1)

if a== -1 or b == -1:
    print(-1)
else:
    print(b-a+1)