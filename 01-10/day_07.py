#Challenge 7: A String Range
def string_range(num):
    return ".".join(map(str,range(num)))

#Extra Challenge: Dictionary of Names
def s_names(names):
    return {i:names.count(i) for i in {n for n in names if n[0] == "S"}}

print(string_range(6))
print(string_range(20))

print(s_names(["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]))
print(s_names(["Sally","Sally", "Sally", "Sally", "Salli", "Jabulani", "Sera", "Patel", "Sera"]))
print(s_names(["Anne", "Peter", "Bob", "Paul"]))
print(s_names(["Steven"]))
