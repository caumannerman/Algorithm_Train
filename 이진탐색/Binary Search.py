''' Binary Search는 정렬된 상태에서 사용할 수 있는 알고리즘이다.

     *** 구현 시 기억해야 할 Point ***

          1. start > end 면 target이 배열에 없는 것!
          2. if - elif - else
          3. 반복문 - 매개변수는 (배열, 타깃)   //  재귀 - 매개변수는 (배열,타깃,start, end)

'''

# 시작점, 끝점을 잡고, 버림하여 중간점 ( 시작0 끝9 --> 중간점 4 )
# 중간점과 찾으려는 값 비교. 중간점이 더 크다면 끝점을 중간점-1, 중간점이 더 작다면, 시작점을 중간점 +1

""" 시간복잡도는 O(logN)이다. """

# 이진탐색 구현에는 두가지 방법이 있다
# 1. 재귀함수 이용
# 2. 반복문 이용

# 12.5 Bin_Search_Iter
'''
array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def bin_search(array, target):
    start = 0
    end = len(array)-1

    while True:
     # 이곳을 start >= end가 아니라 start > end로 해주는 이유는, 다음과 같다
     # start = 4, end = 5 인 상태고, target =5라고 생각해보자.
     # mid = (4+5) //2 로 4가 되고, 아래의 else문에 의해 start = mid +1 즉, start 는 5가 되어 start = end = 5가 된다.
     # 다시 한번 돌아와 mid = (5+5) //2 가 되어 mid = 5가 되고,  array[mid] == target이 되어 return mid로 정상종료가 된다.
     # 즉, start == end인 상태는 아직 함수가 mid를 반환하며 종료할 수 있는 가능성이 열려있는 상태이므로 target이 array에 없다고 보장할 수 없다.
     if start > end:
         return None

     mid = (start + end) // 2
     if array[mid] == target:
         return mid

     elif array[mid] > target:
         end = mid -1
     else:
         start = mid + 1



print(bin_search(array1, 17))
'''

#12.5 Bin_Search_Recursive
'''
array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# 재귀적으로 호출할 것이므로, start, end가 매개변수로 전달되어야한다.
def BS(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BS(array, target, start, mid-1)
    else:
        return BS(array, target, mid + 1, end)

print(BS(array1,16, 0, len(array1)-1))
'''