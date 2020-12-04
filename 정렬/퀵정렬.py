'''기준 데이터를 설정하고 기준보다 큰 데이터와 작은데이터의 위치를 바꾸는게 퀵정렬 '''
# 정렬 라이브러리의 근간이 됨! 병합정렬,퀵정렬이 근본이다. -> 기본은 가장 첫 데이터를 기준(pivot)으로 설정함


# 첫 데이터를 기준으로 잡고 퀵정렬 -> 파티션 -> 왼쪽,오른쪽을 각각 퀵정렬 -> 파티션 이렇게 재귀적으로 수행!

array = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]

'''매개변수로 start, end를 줘야 재귀적으로 호출을 하기 쉽다! ( 그렇지 않으면 새로운 array를 새로운 공간에 할당해서 호출해야함) '''

# 중요한 점 정리

def quick(array, start, end):

# start >= end 인 이유.   start > end 뿐 아니라, start == end 이면, 원소가 하나이므로 정렬할 이유가 없기 때문. 단순 return 해줌
    if start >= end:
        return
# Point : pivot을 array[start]로 해주지 않고, left, right와 함께 인덱스로, 즉 pivot= start로 저장해주는 것이 좋다
    pivot = start
    left = start +1
    right = end
# while left <= right로 해도 좋다. 밑의 코드에서는 이 조건을 벗어나면 break되게 해주었다.
    while True:   ##### 중요!!!
        #  array[right] > array[pivot]으로 해주면, 피벗과 중복된 값이 array에 있을 경우, pivot보다 작은 값들 뿐 아니라 pivot과 같은 값도 자리를 바꿔주게 되는데,
        # pivot과 같은 값들은 굳이 연산을 해주지 않아도 되기 때문에, 등호를 포함시켰다. 하지만 여기서 문제가 생긴다.
        # 등호를 포함시키지 않으면, right가 pivot보다 더 왼쪽으로 갈 걱정이 없다. 왜냐하면, right가 pivot에 도달했을 때 더이상 -1 되지 않기 때문
        # 하지만 아래와 같이 등호가 포함되면, pivot도 넘어 right가 pivot-1까지 갈 수도 있기에, right > start라는 조건이 추가적으로 붙은 것.
        while array[right] >= array[pivot] and right > start:
            right -= 1
        # left <=end를 보고 left 가 end 를 넘어가게 되면 안되는거 아닌가? 하는 생각이 들 수 있지만,
        # left 가 end를 넘어 end+1이 되면, 아랫쪽의 else문에 걸리게 되고, 함수 호출이 끝나게 되며, 그 과정에 left를 사용하는 일이 없어서 상관 없다.
        # 그럼 left < end 로 나타내면 안되는 이유가 있을까 ?
        # 정렬 대상인 array의 원소들이 모두 pivot보다 작다면, right는 end를 가리키고, left는 이 주석 바로 밑의 while문 한번으로 단숨에 end를 가리키게 된다.
        # left < right로 인해 left와 right는 같이 end를 가리키게 되고, 아래의 if문을 한 번 돌고 다시 아래의 while문으로 돌아오면, left는 없는 인덱스(end+1)를 가리켜,
        # error를 보내게 된다.
        # 이 뿐 아니라, left 와 right가 end에서 만났다는 상황 자체가 이미 더이상 연산이 의미 없고, pivot을 end와 바꿔주면 되는 상황이기에,
        # 바로 아래의 else문으로 보내주는 것이 좋기에, left <= end로 나타내주는 것이 좋다. ( 넘어갈거면 빨리 넘겨주기 )
        while array[left] <= array[pivot] and left <= end:
            left += 1
    # 사실 등호는 일어날 경우가 없다 ( while문의 조건을 위와 같이 걸어주었다면 )
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    # 엇갈리는 경우에만 종료.
        else:
            array[start], array[right] = array[right], array[start]
            quick(array, start, right - 1)
            quick(array, right + 1, end)
            break

quick(array, 0, len(array)-1)

print(array)

















# 파티션(분할) 이 반반으로 될 지 아닐지는 모른다. 반반씩 파티션된다고 가정하면 시간복잡도가 O(NlogN)이 됨!!

