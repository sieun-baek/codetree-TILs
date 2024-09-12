i = input().split()
a = int(i[0])
b = int(i[1])

for i in range(a, b+1):
    if a % 2 != 0:
        print(a, end = " ")
        a += 1
    else:
        a += 1