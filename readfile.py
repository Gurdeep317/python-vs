# Program Read a File Line by Line Into a List
with open("helo.txt") as f:
    content_list = f.readlines()
# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)
