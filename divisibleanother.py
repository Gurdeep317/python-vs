print("the number is divisible by 13 is:")
for i in range(1,100):
    if i%13==0:
        print(i)

print()
l=[66,39,48,98,26,87,67]
result=list(filter(lambda x:x%13==0,l))
print("the numbers divisible by 13 is:",result)
