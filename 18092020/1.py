string = input()

if string.isupper():
    print(string)
elif len(string) == 0 or not string.isalpha():
    print(True)

