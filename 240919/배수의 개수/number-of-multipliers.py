cnt = 0
cnt1 = 0
for i in range(10):
    i = int(input())
    if i % 3 == 0:
        cnt += 1
    if i % 5 == 0:
        cnt1 += 1
print(cnt, cnt1)