A , B = map(int,input().split())
C = int(input())
if B + C >=60:
    if A + ((B+C)//60) >= 24:
        A = (((B + C)//60) + A) % 24 
        B = (B + C) % 60
        print(f"{A} {B}")
    else :
        A = A + ((B+C)//60)
        B = (B + C) % 60
        print(f"{A} {B}")
else : 
    A = A 
    B = B + C
    print(f"{A} {B}")