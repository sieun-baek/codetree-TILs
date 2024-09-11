A = input().split()
B = input().split()

am = int(A[0])
ae = int(A[1])
bm = int(B[0])
be = int(B[1])

if am > bm:
    print("A")
elif am < bm:
    print("B")
else:
    if ae > be:
        print("A")
    else:
        print("B")