s = 0
n = 0

while True:
    i = int(input())
    if i <= 29 and i >= 20:
        s += i
        n += 1
    else:
        avg = s / n
        break

print(f"{avg:.2f}")