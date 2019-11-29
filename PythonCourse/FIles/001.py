with open("file.txt", "w+") as file:
    file.write("snail")
    content = file.read()

with open("file.txt") as file:
    content= file.read()
    print(content)
