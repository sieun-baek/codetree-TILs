i = input().split()
a = int(i[0])
b = int(i[1])
c = int(i[2])

if a <= b and a <= c:
    print(1, end = " ")
else:
    print(0, end = " ")
if a == b and b == c:
    print(1, end = " ")
else:
    print(0, end = " ")