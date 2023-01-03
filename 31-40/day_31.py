#Challenge 31: Longest Word
def longest_word(words):
    return max(([len(w),w] for w in words))
    #Thanks Zadok

#Extra Challenge: Create User
def create_user():
    a,b,c = ['Input your first name: ', 'Input your age: ', 'Input your desired password: ']
    user = {'name': input(a), 'age': input(b), 'password': input(c)}
    print('User saved. Please login')
    
    while True:
        correct_input = all([input('Enter your first name: ') == user['name'],
                        input('Enter your password: ') == user['password']])
        if correct_input:
            return 'Logged in successfully'
        print('Wrong password or user name. Please try again')

print(longest_word(['Java', 'JavaScript', 'Python']))

print(create_user())
