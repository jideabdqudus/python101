with open("my_note.txt", mode="r") as file:
    contents = file.read()
    print(contents)


with open("my_note.txt", mode="w") as file:
    file.write("\nWritten into you")

with open("my_note.txt", mode="a") as file:
    file.write("\nAppended into you")