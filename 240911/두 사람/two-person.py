a = input().split()
b = input().split()

aa = int(a[0])
ag = a[1]
ba = int(b[0])
bg = b[1]

if (aa >= 19 and ag == "M") or (ba >= 19 and bg == "M"):
    print(1)
else:
    print(0)