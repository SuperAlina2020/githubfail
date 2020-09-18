list = [1,2,3,4,5]

if len(list) > 1:
    list.insert(len(list), list[0])
    list.pop(0)
    print(list)
elif len(list) == 0 or len(list) == 1:
    print(list)
