

# 12.5선택정렬
"""
list1 = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]

for i in range(len(list1)):
    min_i = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_i]:
            min_i = j
    list1[i], list1[min_i] = list1[min_i], list1[i]



print(list1)
"""

# 12.5 삽입정렬
'''
array = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]

for i in range(1,len(array)):
    for j in range(0, i):
        if array[j] > array[i]:
            temp = array[i]
            for k in range(i-1, j-1, -1):
                array[k+1] = array[k]
            array[j] = temp
            break

print(array)
'''

#12.5 퀵 정렬

'''
array = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]

def quick(array, start, end):


    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end


    while True:
        while array[right] >= array[pivot] and right > start:
            right -= 1
        while array[left] <= array[pivot] and left <= end:
            left += 1

        if left <= right:
            array[right] = array[left]
            left += 1
            right -= 1
        else:
            array[right] ,array[start] = array[start], array[right]
            quick(array, start, right-1)
            quick(array, right+1, end)
            break

quick(array, 0,len(array)-1)
print(array)
'''

#12.5 quicksort
'''
array = [5,7,9,0,3,1,6,2,4,8,1000,3.5,27,45,4,5]

def quick(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick(left)+[pivot]+ quick(right)

print(array)
quick(array)
print(quick(array))
'''


# 12.5 계수정렬
'''
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]*(len(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for j in range(len(count)):
    for k in range(count[j]):
        print(j, end = ' ')
'''
