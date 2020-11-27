list = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]



for j in range(len(list)-1):

    index = j
    for i in range(j+1, len(list)):
         if list[index] > list[i]:
             index = i
    list[index], list[j] = list[j], list[index]  ### Go언어에서처럼 매개체 없이 둘이 서로 값을 바꿀 수 있음.

print(list)


# 선택정렬은 N+ n-1 + n-2 + n-3 + n-4 .....+2 번의 계산을 하기때문에 시간복잡도는 O(N^2)이다!

