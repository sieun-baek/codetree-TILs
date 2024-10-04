n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
s = False

for i in range(a, b+1):
    if i % c == 0:
        s = True
        break
if s == True:
    print("NO")
else:
    print("YES")