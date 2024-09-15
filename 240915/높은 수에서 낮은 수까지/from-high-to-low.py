s = input().split()
a = int(s[0])
b = int(s[1])


if a >= b:
    for i in range(a, b+1):
        print(a, end=' ')
        a -= 1
else:
    for i in range(a, b+1):
        print(b, end=' ')
        b -= 1