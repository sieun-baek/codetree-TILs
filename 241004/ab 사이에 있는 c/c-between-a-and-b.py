n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
cnt = 0

while True:
    for i in range(a, b):
        if i % c == 0:
            cnt += 1
    break

if cnt >= 1:
    print("YES")
else:
    print("NO")