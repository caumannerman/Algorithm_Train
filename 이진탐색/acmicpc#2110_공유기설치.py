"""도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
# 출력 : 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.


'''주인공을 무엇으로 생각하냐.. 그 아이디어를 떠올리기 매우 어려운 문제.
    이분탐색을 해야될 것 같은데, 이분탐색을 어디에 사용해야할지 감이 안 오는 문제.
    
    우리는 주인공으로 공유기를 설치할 "최소의 간격" 으로 두고, 이 최소 간격의 범위를 1~ (맨 앞의 집 ~ 맨 뒤 집 사이 거리) 로 두고 이진탐색을 해야한다.
    해당 최소간격으로 c보다 많거나 같은 수의 집에 공유기를 설치할 수 있다면 기록해두고 넘어간다. 
    ==> c개의 집에 공유기를 설치하고 싶을 때, 두어야하는 최소의 간격의  최대치를 구할 수 있다.'''
import sys
input = sys.stdin.readline
n ,c = map(int, input().split())

zip = []
for _ in range(n):
    zip.append(int(input()))
# 이분탐색을 하기위해 sort
zip.sort()

# chai라는 차이를 최소간격으로 했을 때, 공유기를 설치할 수 있는 최대 집 수
def counthoust(data, chai):
    count = 1
    old = data[0]
    for i in range(1, len(data)):
        if data[i] - old >= chai:
            old = data[i]
            count += 1
            if count > c:
                return -1
    return count

def bs(data):
    start = 1
    end = zip[-1] - zip[0]
    last = -1
    while True:
        mid = (start + end) // 2
        now = counthoust(zip,mid)
        if now == -1:
            last = mid
            start = mid + 1
        elif now < c:
            end = mid - 1
        else:
            last = mid
            start = mid + 1
        if start > end:
            break
    return last

print(bs(zip))