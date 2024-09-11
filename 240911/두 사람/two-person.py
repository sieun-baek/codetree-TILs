a = input().split()
b = input().split()

aa = int(a[0])
ag = a[1]
ba = int(b[0])
bg = b[1]

if (aa and ba) < 19 or (ag and bg) == "M":
    print(0)
else:
    print(1)