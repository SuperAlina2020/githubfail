a = list(map(int,input().split()))
max = 1
i = 0
while i < len(a) :
    if a[i] > max :
        max = a[i]
    i = i + 1
j = 0
check = 0
check1 = 0
b = []
while j < len(a):
    check = max - a[j]
    j = j + 1
    b.append(check)
x = 0
maximum = 0
while x < len(b):
    if b[x] >= maximum:
        maximum = b[x]
    x =  x + 1
print(maximum)
link1 = b.index(maximum)
link2 = a[link1]
print(link2)













