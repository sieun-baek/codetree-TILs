n = int(input())
c = False

for i in range(2, n):
    if n % i == 0:
        c = True

if c == True:
    print('C')
else:
    print('N')