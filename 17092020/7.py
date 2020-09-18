password = input()
with open('text.txt','w') as file1:
    file1.write(password)
if len(password) > 6:
    print(True)
    with open('text.txt','a') as file1:
        file1.write("True")

else:
    print(False)
    with open('text.txt','a') as file1:
        file1.write("False")