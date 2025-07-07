N = int(input())
a = "*"
b = " "
for i in range(1,N+1,1):
    print(f"{b*(N-i)}{a*i}")