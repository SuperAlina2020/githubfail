len_list = int(input())
new_list = []

for i in range (len_list):
    new_elem = int(input())
    new_list.append(new_elem)
print(new_list)
new_list1 = []
for i in range(3):
    if i == 0:
        new_list1.append(new_list[0])
    elif i == 1:
        new_list1.append(new_list[2])
    else:
        new_list1.append(new_list[-2])
print(new_list1)

