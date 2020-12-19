data = [9, 3, 5, 6, 2, 1, 8, 4, 7,100,0.3, 1251, 99, 45,32,5412]


for i in range(1, len(data)):
    for j in range(0, i):
        if data[i] < data[j]:
            temp = data[i]
            for k in range(i, j, -1):
                data[k] = data[k-1]
            data[j] = temp
            break

print(data)