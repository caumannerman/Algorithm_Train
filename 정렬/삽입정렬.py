# 선택정렬보다 효율적. // 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입함.
# 삽입정렬도 O(N^2)의 시간복잡도. 마찬가지로 반복문 두번 중첩
# 현재 리시트의 데이터가 거의 정렬돼있는 상태면 매우 빠르게 동작한다. -> 최선의 경우 O(n)의 시간복잡도
list = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]
array = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]
#이게 내가만든 코
'''   이게 내가 만든 코드  
for i in range(1,len(list)):
    temp = list[i]
    for j in range(0,i):
        if list[i] > list[j]:
            continue
        else:
            for k in range(i-1, j-1, -1):
                list[k+1] = list[k]
            list[j] = temp

print(list)

'''

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j-1], array[j]
        else:
            break

print(array)


