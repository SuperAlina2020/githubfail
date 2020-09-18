sentence = input()
sentence = sentence.capitalize()
if sentence[-1] == '.':
    print(sentence)
else:
    sentence = sentence + '.'
    print(sentence)