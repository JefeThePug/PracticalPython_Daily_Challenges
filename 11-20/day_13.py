import emoji #requires pip install

#Challenge 13: Pay Your Tax
def get_number(percent = False):
    msgs = ('Input item price: ','Input VAT percentage: ')
    num = None
    while not num:
        n = input(msgs[percent])
        replace = n.maketrans('','','% $¥£€₹₱₣₩')
        n = n.translate(replace)
        try:
            num = float(n)
        except ValueError:
            print('Please input a valid number')
        else:
            if percent and num > 100:
                print('Please input a correct percentage.')
                num = None
    return num
        
def your_vat():
    price = get_number()
    vat = get_number(True)/100
    return f'{(price * vat + price):,.2f}'

#Extra Challenge: Pyramid of Snakes
def python_snakes(n):
    for i in range(n):
        print(emoji.emojize(':snake:'*i))
        
def python_snakes2(n):
    for i in range(n):
        print(emoji.emojize(':snake: '*i).center(2*n,' '))

        
print(your_vat())

#more of a slant
python_snakes(7)
#more of a pyramid
python_snakes2(10)
