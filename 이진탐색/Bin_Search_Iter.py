
#이미 정렬된 리스트
array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# target이 몇 번 째 인덱스에 있는지 그 번호를 return 해준다
def BS(array, target):

    start = 0
    end = len(array)-1

    while True:
        mid = (start + end) //2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

        if start > end:
            return None


target = int(input("찾고자 하는 숫자를 입력하세요 : "))

result = BS(array1, target)
if result == None:
    print("해당 target은 존재하지 않습니다!")

print(result, "번 째 인덱스에 위치해있음")

