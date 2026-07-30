"""Find the most frequent word."""
Text = list(map(str,input("Enter Text:").split()))

word_count = {}

for word in Text:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] = 1

most_frequent_word = max(word_count, key = word_count.get)
print("Most Frequent Word:", most_frequent_word) # shows first occured word

max_frequent = max(word_count.values())

result = min(word for word,count in word_count.items() if count == max_frequent)
print(result) #shows lexicographic smaller word

all_result = [word for word,count in word_count.items() if count == max_frequent]
print(all_result) # shows all words with same frequency
