a = 0
x = int(input())

if x > 1 and x < 1000000:
    if x % 5 == 0:
        x = x // 5
        print(x)
    elif x % 5 != 0:
        x = x // 5
        print(x+1)
