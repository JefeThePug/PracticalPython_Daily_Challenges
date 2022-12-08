#Challenge 5: My Discount
def my_discount():
    price = int(input("Input the price: "))
    discount = int(input("Input the discount: ").replace("%",""))
    return price - price * discount / 100

#Extra Challenge: Tuple of Student Sex
#with Counter
def male_and_female(students):
    from collections import Counter
    corrected = map(lambda x: x.title(), students)
    return list(Counter(corrected).items())

#without Counter
def male_and_female2(students):
    nums = [0,0]
    for student in students:
        if len(student) == 4:
            nums[0]+=1
        else:
            nums[1]+=1
    return list(zip(["Male","Female"], nums))

#shorter but hacky
def male_and_female3(students):
    nums = [0,0]
    for student in students:
        nums[len(student)//2-1] += 1
    return list(zip(["Male","Female"], nums))

print(my_discount())
                
print(male_and_female(['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))
print(male_and_female2(['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))
print(male_and_female3(['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))
