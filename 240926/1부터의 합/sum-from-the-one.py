n = int(input())
cnt = 0
s = 0

for i in range(1, 101):
    s += i
    if s >= n:
        cnt += i
        break
print(cnt)