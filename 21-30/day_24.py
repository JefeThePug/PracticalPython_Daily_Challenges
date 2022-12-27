#Challenge 24: Average Calories
def get_daily_calories(num):
    while True:
        cals = input(f'Enter your total calories for day {num} or input "done" to quit:')
        try:
            res = int(cals)
        except ValueError:
            if cals.strip().lower().replace('"','') == 'done':
                return 'Q'
            print('Please just enter a number, or the word "done" to quit.')
        else:
            return res

def average_calories():
    day = 1
    calories = []
    while True:
        cals = get_daily_calories(day)
        if cals == 'Q': break
        calories.append(cals)
        day += 1
    summary = ', '.join(map(lambda x: f'Day {x[0]}: {x[1]} Calories', enumerate(calories,1)))
    average = sum(calories)/len(calories) if calories else 0
    return summary, f'Average: {average} Calories'
        

#Extra Challenge: Create a Nested List
def nested_lists(*args):
    return list(args)

print(*average_calories(), sep='\n')

print(nested_lists([1,2,3,5],[1,2,3,4],[1,3,4,5]))
print(nested_lists([1,2,3,4,5,6,7,8]))
