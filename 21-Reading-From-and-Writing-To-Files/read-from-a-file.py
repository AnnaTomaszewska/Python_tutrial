with open("cupcakes.txt", "r") as cupcakes_file: 
    print("The text has been opened!")
    content = cupcakes_file.read()
    print(content)

print("The file has been closed!")

filename = input("What file would you like to open? ")
with open(filename, "r") as file_object:
    print(file_object.read())
