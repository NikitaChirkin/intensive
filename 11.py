a = int(input())
p = 1
while a != 0:
    ost = a % 10
    print(ost)
    p = p * ost
    print(p)
    a = a // 10
    print(a)
print(p)
