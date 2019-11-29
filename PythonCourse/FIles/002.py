with open("bear.txt") as file:
    content = file.read()
    content = content[:90]

with open("file.txt", 'w') as file:
    file.write(content)