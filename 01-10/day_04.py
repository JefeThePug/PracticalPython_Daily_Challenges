#Challenge 4: Only Floats
def only_floats(a, b):
    return sum(isinstance(i, float) for i in (a,b))

#Extra Challenge: Index of the Longest Word
def word_index(words):
    """for Xarlos:
    return 0 if len((s:=sorted(words,key=len,reverse=True))[0]) == len(s[1]) else words.index(s[0])
    """
    s_words = sorted(words,key=len,reverse=True)
    long_i = words.index(s_words[0])
    return 0 if len(s_words[0]) == len(s_words[1]) else long_i

print(only_floats(12.1,23))
print(only_floats(12.5,23.6))
print(only_floats(12,23))

print(word_index(["Hate", "remorse", "vengeance", "ire"]))
print(word_index(["Love", "Hate"]))
