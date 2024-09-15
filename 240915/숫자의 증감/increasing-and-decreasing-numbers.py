a = input().split()
c = a[0]
n = int(a[1])

if c == 'A':
    for i in range(1, n+1):
        print(i, end = '')
        i += 1
else:
    for i in range(n-1, 1, -1):
        print(n, end = '')
        n -= 1