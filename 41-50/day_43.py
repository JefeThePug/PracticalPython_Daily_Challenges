#Challenge 43: Student Marks
def student_marks():
    marks = {}
    while True:
        name = input("Input student's name or 'done' to stop: ")
        if name.lower().replace("'","").strip() == 'done': break
        marks[name] = [*map(float,input(f"Input {name}'s marks, separated by spaces: ").split())]
    return marks

print(student_marks())
