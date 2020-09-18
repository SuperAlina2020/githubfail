string = input()
a = []
for i in string:
    a.append(i)
j = 0
while j < len(a):
    if a[j] == 'A':
        a[j] = 'B'
    elif a[j] == 'B':
        a[j] = 'A'
    j = j + 1
for line in a:
    print(line,end='')
