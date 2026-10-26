with open("students.txt", "r") as file:
 content = file.read()
print(content)


#new comments file
with open("students.txt", "r+") as file:
    content = file.read()
    file.seek(0)
    file.write(" God is good ")
    
    print(content)

