# program to count the number of each vowel
# taking a string as a
# taking vowels as variable which contain all variable
# then using casefold in a
# then take a count variable and apply keys on vowel
# using for loop and if condition


a="harry Potter"
vowels="aeiou"
a=a.casefold()
count={}.fromkeys(vowels,0)
for char in a:
    if char in count:
        count[char]+=1
print(count)