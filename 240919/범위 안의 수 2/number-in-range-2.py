cnt = 0
n = 0

for i in range(10):
    i = int(input())
    if i >= 0 and i <= 200:
        cnt += i
        n += 1

avg = cnt / n
print(cnt, round(avg, 1))