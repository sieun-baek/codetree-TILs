a = input().split()
b = input().split()

aa = int(a[0])
ag = a[1]
ba = int(b[0])
bg = b[1]

if (ag or bg) == "M" and (aa or ba) >= 19:
    print(1)
else:
    print(0)