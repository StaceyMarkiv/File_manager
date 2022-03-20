import sys


s1 = [1, 2, 3, 4, 5]
s2 = []
s3 = []
for i in range(len(s1) - 1):
    result = s1[i] + s1[i+1]
    s2.append(result)

A = 999
for B in s1:
    if A != 999:
        s3.append(A + B)
    A = B


print(s1)
print(s2)
print(s3)
sys.exit(-1)