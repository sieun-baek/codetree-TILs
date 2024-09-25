n = int(input())
sum1 = 0

for i in range(n):
    i = int(input())
    sum1 += i
avg = sum1 / n

print(sum1, round(avg, 1))