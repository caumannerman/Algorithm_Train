t = int(input())
data = []
for _ in range(t):
    w = list(input())
    k = int(input())
    data.append((w, k))

albet = [[] for _ in range(26)]


def solution(temp, albet, k):
    s_result = 100000
    r_result = -1

    for i in temp:
        for j in range(k - 1, len(albet[i])):
            if albet[i][j] - albet[i][j - k + 1] < s_result:
                s_result = albet[i][j] - albet[i][j - k + 1]
            if albet[i][j] - albet[i][j - k + 1] > r_result:
                r_result = albet[i][j] - albet[i][j - k + 1]
    print(s_result + 1, r_result + 1)


for i in data:
    for j in range(len(i[0])):
        albet[ord(i[0][j]) - ord('a')].append(j)
    temp = []
    for k in range(len(albet)):
        if len(albet[k]) >= i[1]:
            temp.append(k)
    if not temp:
        print(-1)
    else:
        solution(temp, albet, i[1])
        albet = [[] for _ in range(26)]