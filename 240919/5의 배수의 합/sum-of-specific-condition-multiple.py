n = input().split()
a = int(n[0])
b = int(n[1])
cnt = 0

if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            cnt += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            cnt += i

print(cnt)