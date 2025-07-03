a = int(input())
b = int(input())
c = b % 10
d = (b % 100 - c)//10
e = b//100
print(f"{a*c}\n{a*d}\n{a*e}\n{a*b}")