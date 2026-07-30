""" First non repeating character """

example = input("Enter Text")
char_count ={}
for char in example:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

for key,val in enumerate(char_count.items()):
    print(key,val)

for char in example:
    if char_count[char]==1:
        print("First non repeating character:", char)
        break
