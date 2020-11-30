array1 = [5,7,9,0,3,1,6,2,4,8,1000,3.5,27,45,4,5]

def quick(array): # 이 경우에는 매개변수로 array만 받을 것이다. 컴프리헨션을 사용하게 되면,
    # 피벗을 기준의 좌, 우측에서 새로운 리스트를 생성해야하고, 그 자체를 매개변수로 넘겨줄 것이기 때문.

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick(left)+[pivot]+quick(right)



print(quick(array1))

print(array1)


#  이 경우는 원본을 건드리지 않는다는 특징이 있다.