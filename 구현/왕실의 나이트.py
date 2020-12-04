import timeit



pos = list(input())


start = timeit.default_timer()
# 측정 할 코드는 여기에 둔다.
'''
xpos, ypos = int(pos[1]), ord(pos[0])



count = 0

for i in (2,1):
    for j in (1,-1): # x는 2, -2, 1,-1 순이다.
        for k in (-1,1):
            if xpos + i*j > 0 and xpos + i*j < 9 and ypos + (3-i)*k > 96 and ypos + (3-i)*k < 105:
                count += 1



print(count)
'''

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

stop = timeit.default_timer()

# s(초) 단위로 나온다.
print(stop - start)