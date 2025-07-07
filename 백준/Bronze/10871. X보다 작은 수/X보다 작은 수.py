N , X = map(int, input().split())
a = list(map(int, input().split()))
b = 0
for i in range(N):
    if a[i] < X:
        b = a[i]
        print(b,end=" ")        
        