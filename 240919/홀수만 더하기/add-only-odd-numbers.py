n = int(input())
cnt = 0

for i in range(n):
    i = int(input())
    if i % 2 != 0 and i % 3 == 0:
        cnt += i

print(cnt)