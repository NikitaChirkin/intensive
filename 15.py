n = int(input())
d = int(input())
flag = False
while n != 0:
    ost = n % 10
    n = n // 10
    if ost == d:
        flag = True
print(flag)