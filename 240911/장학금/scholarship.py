i = input().split()
m = int(i[0])
f = int(i[1])

if m >= 90:
    if f >= 95:
        print(100000)
    elif f >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)