a="harry Potter"
vowels="aeiou"
a=a.casefold()
count={}.fromkeys(vowels,0)
for char in a:
    if char in count:
        count[char]+=1
print(count)