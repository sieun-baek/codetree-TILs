A = input().split()
B = input().split()
a_m = int(A[0])
a_e = int(A[1])
b_m = int(B[0])
b_e = int(B[1])

if a_m > b_m and a_e > b_e:
    print(1)
else:
    print(0)