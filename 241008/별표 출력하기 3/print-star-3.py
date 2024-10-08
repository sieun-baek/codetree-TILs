n = int(input())

for i in range(n-1, -1, -1):
    for j in range(2*(n-1) - 2*i):
        print(' ', end = '')
    
    for j in range(i*2+1):
        print('*', end=' ')
    print()

       # i j ''
       # 3 7 0
       # 2 5 2
       # 1 3 4
       # 0 1 6
       # j = i*2+1
       # '' = 2n - 2i