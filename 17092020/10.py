a = [1,2,3,4,5]
num = int(input())

j = 0

if num in a:
    index_elem = a.index(num)
    while j < index_elem:
        a.pop(0)
        j = j + 1
    print(a)
elif num not in a:
    print(a)
elif len(a) == 0:
    print(a)



