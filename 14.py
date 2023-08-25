n = int(input())
digital_max = -1
digital_min = 10
while n != 0:
    ost = n % 10
    n = n // 10
    if ost > digital_max:
        digital_max = ost
    if ost < digital_min:
        digital_min = ost
print(digital_max)
print(digital_min)

