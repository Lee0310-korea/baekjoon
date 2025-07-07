X = int(input())
N = int(input())
C = 0
D = 0
for i in range(1,N+1,1):
    a,b = map(int,input().split())
    C = a * b
    D += C

if D == X :
    print("Yes")
else :
    print("No")