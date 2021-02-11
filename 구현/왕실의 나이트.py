"""풀이1"""
pos = list(input())


dx = [2,2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
count = 0
for i in range(8):
    if ord(pos[0]) + dx[i] >= ord('a') and ord(pos[0]) + dx[i] <= ord('h') and int(pos[1]) + dy[i] >= 1 and int(pos[1]) + dy[i] <= 8:
        count += 1


print(count)


""" 풀이 2
row = int(pos[1])
column = int (ord(pos[0])) - int(ord('a')) +1

steps = [(-2,-1), (-2,1), (2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

result = 0
for step in steps:
    next_row = row +step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)
"""


''' 풀이 3
xpos, ypos = int(pos[1]), ord(pos[0])

count = 0

for i in (2,1):
    for j in (1,-1): # x는 2, -2, 1,-1 순이다.
        for k in (-1,1):
            if xpos + i*j > 0 and xpos + i*j < 9 and ypos + (3-i)*k > 96 and ypos + (3-i)*k < 105:
                count += 1
print(count)
'''