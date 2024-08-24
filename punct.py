# program to remove punctuations from a string
# taking a string from user
# using for loopusing if condition
punc='''~!@#$%^&*()_+=-<>?:"|,./;'][]\{}'''
string =input("enter anything here:")
emptystring=""
for i in string:
    if i not in punc:
        emptystring+=i
print(emptystring)