# Program to Sort a Dictionary by Value 
# taking a dictionary and then sort it
# taking a temporary function lambda
# solution 1 sort the dictionary based on value
marks={"meena":43,"riya":35,"annu":87}
print(marks)
# sorted=sorted(marks.items(),key=lambda x:x[1])
# print(sorted)

# solution 2 sort only by values
# sorted the marks
sort=sorted(marks.values())
print(sort)