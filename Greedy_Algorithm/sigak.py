n = int(input())



if n < 3:
    x = n + 1
elif n < 13:
    x = n
elif n < 23:
    x = n - 1
else:
    x= n - 2

print( 3600*n + 3600 - x*45**2)



# 이것도
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)
