while True:
    i = input().split()
    a = int(i[0])
    b = int(i[1])
    t = (i[2])
    if t != 'C':
        print(a*b)
    elif t == 'C':
        print(a*b)
        break