H,M = map(int,input().split())

if M-45 < 0 :
    if H-1<0:
        H=23
        M=M+60-45
        print(f"{H} {M}")
    else :
        M=M+60-45
        print(f"{H-1} {M}")
else :
    print(f"{H} {M-45}")