N = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for i in range(N):
    if i == 0 :
        b = a[i]
        c = a[i]
    elif b < a[i]:
        b = a[i]
    elif c > a[i]:
        c = a[i]
print(f"{c} {b}")
