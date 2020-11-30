

array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# target이 몇 번 째 인덱스에 있는지 그 번호를 return 해준다
def BS(array, target, start, end):
    if start > end :
        return None
    mid = (start + end)//2
    '''if start == end and array[start] != target:
        return None'''
    """넣어줬던 위의 주석처리한 코드를 넣어주지 않아도 되는 이유 : array에 target이 없다면, 결국 start와 end는 바로 옆에서 만나고, 같아지고, 결국 start가 end보다 커진"""
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BS(array, target, start, mid-1)
    else:
        return BS(array, target, mid + 1, end)



target = int(input("찾고자 하는 숫자를 입력하세요"))

result = BS(array1, target, 0,len(array1)-1)

if result == None:
    print("원소가 존재하지 않음")
else:
    print(result, "번 째 인덱스에 위치해있음")