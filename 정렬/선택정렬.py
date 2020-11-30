
''' 선택정렬 ( Selection Sort ) -> 매번 가장 작은 것을 선택하여 앞으로 보냄'''

list1 = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]




# 선택정렬은 N+ n-1 + n-2 + n-3 + n-4 .....+2 번의 계산을 하기때문에 시간복잡도는 O(N^2)이다!

for i in range(len(list1)):
    min_index = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_index]:
            min_index = j
    list1[i], list1[min_index] = list1[min_index], list1[i] ### Go언어에서처럼 매개체 없이 둘이 서로 값을 바꿀 수 있음.

print(list1)