A,B,C = map(int, input().split())
D = 0
if A != B and B!=C and A != C :
    if A > B and A > C:
        D = A * 100
        print(f"{D}")
    elif B > A and B > C:
        D = B * 100
        print(f"{D}")
    elif C > B and C > A :
        D = C * 100
        print(f"{D}")
elif A==B or B==C or C==A:
    if A==B and B==C and C==A:
        D = A*1000 +10000
        print(f"{D}")
    else :
        if A == B and A != C:
            D = A * 100 + 1000
            print(f"{D}")
        elif C == B and B != A:
            D = B * 100 + 1000
            print(f"{D}")
        elif A == C and B != C:
            D = A * 100 + 1000
            print(f"{D}")    