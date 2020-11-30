'''기준 데이터를 설정하고 기준보다 큰 데이터와 작은데이터의 위치를 바꾸는게 퀵정렬 '''
# 정렬 라이브러리의 근간이 됨! 병합정렬,퀵정렬이 근본이다. -> 기본은 가장 첫 데이터를 기준(pivot)으로 설정함


# 첫 데이터를 기준으로 잡고 퀵정렬 -> 파티션 -> 왼쪽,오른쪽을 각각 퀵정렬 -> 파티션 이렇게 재귀적으로 수행!

array1 = [5,7,9,0,3,1,6,2,4,8,1000,3.5,27,45,4,5]

'''매개변수로 start, end를 줘야 재귀적으로 호출을 하기 쉽다! ( 그렇지 않으면 새로운 array를 새로운 공간에 할당해서 호출해야함) '''
def quick(array, start, end):

    if start >= end:
        return

    pivot = array[start]
    left = start +1
    right = end

    while True:   ##### 중요!!!
        while array[right] > pivot:
            right -= 1

        while array[left] < pivot:
            left += 1
            if left == end+1:
                left -= 1
                break

        if left < right:
            array[left], array[right] = array[right], array[left]
        else:
            array[start], array[right] = array[right], array[start]
            break

    print(array)

    quick(array, start, right-1)
    quick(array, right+1, end)


quick(array1, 0, len(array1)-1)

print(array1)

















# 파티션(분할) 이 반반으로 될 지 아닐지는 모른다. 반반씩 파티션된다고 가정하면 시간복잡도가 O(NlogN)이 됨!!

