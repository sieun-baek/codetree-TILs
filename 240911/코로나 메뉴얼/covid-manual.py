a = input().split()
b = input().split()
c = input().split()

asym = a[0]
atem = int(a[1])
bsym = b[0]
btem = int(b[1])
csym = c[0]
ctem = int(c[1])

if asym == "Y" and atem >= 37:
    if (bsym == "Y" and btem >= 37) or (csym == "Y" and ctem >= 37):
        print("E")
    else:
        print("N")
elif bsym == "Y" and btem >= 37:
    if csym == "Y" and ctem >= 37:
        print("E")
    else:
        print("N")
else:
    print("N")