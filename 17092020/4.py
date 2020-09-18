# второй способ
number = int(input())
string_number = str(number)
a = []
for i in range(len(string_number)):
    a.append(string_number[i])
print(max(a))