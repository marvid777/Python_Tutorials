# with open("example.txt", "w") as fh:
#fh = open("example2.txt", "a")
#fh.write("To write or not to write\nthat is the question!\n")

#fh.close()


with open("example2.txt", "r+") as file:
    text = file.read()
    print(text)
    file.write("das ist das Ende\n")
    text2 = file.read()
    print(text2)




