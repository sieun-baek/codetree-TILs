n = input().split()
h = int(n[0])
w = int(n[1])

b = (10000*w)/h**2

print(int(b))

if b >= 25:
    print("Obesity")