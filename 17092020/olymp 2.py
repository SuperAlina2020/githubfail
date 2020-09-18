x = int(input())
i = 0
if x >= 1 and x <= 100:

    while i < x:
        word = input()
        if len(word) > 10:
            print(word[0],len(word)-2,word[-1],sep='')
        else:
            print(word)

        i = i + 1