n = int(input())
s = False

for i in range(2, n):
    if n % i == 0:
        s = True
        break
if s == True:
    print("C")
else:
    print("P")