''' 하나의 수열에는 다양한 수가 존재한다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만들라 '''
# 첫 째 줄에 수열에 속해있는 수의 개수 N이 주어진다.
# 둘째 줄부터 N+1 번 째 줄까지 N개의 수가 입력되고,   주어진 수열을 내림차순으로 정렬하여 결과를 공백으로 구분하여 출력한다.
import time


n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))



start = time.time()
arr.sort()
arr.reverse()

end = time.time()


for i in arr:
    print(i, end = ' ')
print()
print( end-start)