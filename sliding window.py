"""Find the length of longest substring without repeating characters."""

S = input("Enter Text:")

max_length = 0
char_index = {}
start = 0

if len(S) == 0:
    print("Length of longest substring without repeating characters: 0")
else:
    for end, char in enumerate(S):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] +1
            
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
print("Length of longest substring without repeating characters:", max_length)
print(char_index)

