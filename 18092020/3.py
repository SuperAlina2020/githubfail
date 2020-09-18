# первый способ
num = int(input())
maximum = 0
i = 0
string_number = str(num)
while i < len(string_number):

    int_number = int(string_number[i])
    if int_number > maximum:
        maximum = int_number

    i = i + 1
print(maximum)