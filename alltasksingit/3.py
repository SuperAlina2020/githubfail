a = list(map(int,input().split()))
x = int(input())

check = 0
c = []

for i in a:
    if i > x :
        check = i - x
        c.append(check)
    else :
        check = x - i
        c.append(check)
link = c.index(min(c))
print(a[link])


