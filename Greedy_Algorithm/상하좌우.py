

import timeit


n = int(input())

plan = list(input().split())  # 그냥 input().spllit() 해도, 공백기준으로 잘라서 리스트가 됨!



location = [1,1]  # 굳이 1,1 리스트로 안 놓고, 그냥 x,y로 별개의 변수로 두는 것이 더 효율적일 수도 있다.

for i in plan:
    if i == "R":
        if location[1] < n:
            location[1] = location[1]+1
        else: pass
    elif i == "L":
        if location[1]>1:
            location[1] = location[1]-1
        else: pass
    elif i == "U":
        if location[0]>1:
            location[0] = location[0]-1
        else: pass
    else:
        if location[0] < n:
            location[0] = location[0]+1
        else: pass

print(location[0],location[1])



stop = timeit.default_timer()

# s(초) 단위로 나온다.
print(stop - start)



## 이 문제는 방향이 4군데라서 간단히 엘스이프문으로 나눌 수 있었지만, 종류, 방향이 많아질수록 더 일반화해서 풀어줘야함.
#
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny <1 or nx>n or ny>n:
        continue

    x, y = nx, ny


print(x, y)