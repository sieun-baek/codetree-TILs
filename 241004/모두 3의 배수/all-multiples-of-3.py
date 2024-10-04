s = 1

for i in range(5):
    i = int(input())
    if i % 3 != 0:
        s = 0
        break

print(s)