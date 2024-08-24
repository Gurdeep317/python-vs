punc='''~!@#$%^&*()_+=-<>?:"|,./;'][]\{}'''
a=input("enter anything here:")
emptystring=""
for i in a:
    if i not in punc:
        emptystring+=i
print(emptystring)