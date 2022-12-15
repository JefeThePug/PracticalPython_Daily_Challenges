#Challenge 12: Count the Dots
def count_dots(s):
    return s.count('.')

#Extra Challenge: Your Age in Minutes
def get_year(this_year):
    while True:
        year = input("Enter your four-digit birth year (eg 1988): ")
        if not year.isdigit(): 
            print("Try again with numbers.")
        elif 1900 <= int(year) <= this_year:
            return int(year)
        else:
            print("Input a valid year.")

def age_in_minutes():
    from datetime import date
    this_year = date.today().year
    birth_year = get_year(this_year)
    delta_secs = (date(this_year,1,1) - date(birth_year,1,1)).total_seconds()
    return int(delta_secs/60)

print(count_dots('h.e.l.p.'))
print(count_dots('he.lp.'))

print(age_in_minutes())
