
''' 선택정렬 ( Selection Sort ) -> 매번 가장 작은 것을 선택하여 앞으로 보냄'''

data = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]



# 선택정렬은 N+ n-1 + n-2 + n-3 + n-4 .....+2 번의 계산을 하기때문에 시간복잡도는 O(N^2)이다!

for i in range(len(data)):
    min_idx = i
    for j in range(i+1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i] ### Go언어에서처럼 매개체 없이 둘이 서로 값을 바꿀 수 있음.

print(data)