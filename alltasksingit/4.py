a = [160,155,150,145,140]
height = int(input())
link = 0

for student in a :
    if height > student :
        link = a.index(student)
        a.insert(link,height)
        break
print(a)

