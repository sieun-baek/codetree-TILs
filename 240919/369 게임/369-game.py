n = int(input())

for i in range(1, n+1):
    m = i % 10
    if i % 3 == 0:
        print(0, end=' ')
    elif (m == 3) or (m == 6) or (m == 9):
        print(0, end=' ')
    elif i / 10 == 3:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1