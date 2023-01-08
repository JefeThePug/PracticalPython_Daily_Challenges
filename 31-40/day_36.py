#Challenge 36: Count String
def count_str(s):
    return {c:s.count(c) for c in s.lower()}

print(count_str('hello'))
long_s = """'You can do anything you want to do as long as you keep a good attitude and keep working at it. 
But the second you give up, you’re screwed.' Dolly Parton"""
print(count_str(long_s))