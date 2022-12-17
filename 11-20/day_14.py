#Challenge 14: Flatten the List
def flat_list(nest):
    import re
    return [*map(int,re.sub(r'[\[\]\s]','',f'{nest}').split(','))]

#Extra Challenge: Teacher's Salary
#with function
def your_salary(name, periods):
    standard, overtime = min(100, periods),max(periods - 100, 0)
    rate, ot_rate = 20.0, 25.0
    output = f'Teacher: {name.title()},\n'
    output += f'Periods: {periods}\n'
    output += f'Gross salary: ${(standard * rate + overtime * ot_rate):,.2f}'
    return output

#with class
class Teacher:
    def __init__(self, name, periods):
        self.name = name
        self.periods = min(100, periods)
        self.overtime = max(periods - 100, 0)
        self.rate = 20.0
        self.ot_rate = 25.0
        self.gross_salary = self.get_salary()
        
    def get_salary(self):
        salary = self.periods * self.rate + self.overtime * self.ot_rate
        return salary
    
    def __str__(self):
        output = f'Teacher: {self.name.title()},\n'
        output += f'Periods: {self.periods + self.overtime}\n'
        output += f'Gross salary: ${self.gross_salary:,.2f}'
        return output

print(flat_list([[2,4,5,6]]))
print(flat_list([[1],[2,4,5],[3]]))
print(flat_list([[1],[2,4,5],[3, [3,3,3]]]))

#with function
print(your_salary('john kelly', 105))
#with class
print(Teacher('john kelly', 105))
