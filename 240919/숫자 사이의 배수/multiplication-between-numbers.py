n = input().split()
a = int(n[0])
b = int(n[1])
cnt = 0
j = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        cnt += i
        j += 1


avg = cnt / j

print(cnt, round(avg, 1))