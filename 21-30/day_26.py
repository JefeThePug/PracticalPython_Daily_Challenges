#Challenge 26: Sort Words
def sort_words(s):
    return sorted(set(c for c in s if not c.isspace()))

#Extra Challenge: Length of Words
def string_length(s):
    return {word:len(word) for word in s.split()}

print(sort_words('love life'))

print(string_length('Hi my name is Richard'))
