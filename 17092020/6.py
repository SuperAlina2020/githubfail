text = 'hello world its python programmist im new here'
space = text.index(' ')
print(text[:space])
with open('text.txt','w') as file1:
    file1.write(text[:space])
    