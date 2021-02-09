n = int(input())
jandon = list(map(int, input().split()))

dpTable = [0]*(n+1)

for i in jandon:
    dpTable[i] = 1

for i in range(min(jandon)+ 1, n+1):
    if dpTable[i] == 0:
        temp = []
        for j in jandon:
            if i - j > 0:
                temp.append(dpTable[i-j])
        if max(temp) == 0:
            continue
        temp_min = int(1e9)
        for k in temp:
            if k != 0 and k < temp_min:
                temp_min = k

        dpTable[i] = temp_min + 1

if dpTable[n] == 0:
    print("해당 금액을 완전히 거슬러줄 수 없습니다.")
else:
    print("해당 금액을", dpTable[n],"개의 동전으로 최소한의 갯수로 거슬러줄 수 있습니다.")
    print(dpTable)


