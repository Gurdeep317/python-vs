# program to merge two dictionaries
# taking two dictionaries
# merge using bar operator
# dict1={"hello":34,"welcome":76}
# dict2={"welcome":45,"rao":34}
# print(dict1|dict2)
dict1={"hello":34,"welcome":76}
dict2={"welcome":45,"rao":34}
print({**dict1,**dict2})
