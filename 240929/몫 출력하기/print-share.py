i = 0
sum = 0

while True:
    i = int(input())
    if i % 2 == 0:
        print(i // 2)
        sum += 1
    if sum == 3:
        break