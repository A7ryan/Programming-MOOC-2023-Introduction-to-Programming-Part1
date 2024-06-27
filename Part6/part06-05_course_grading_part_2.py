def read_file(file_name):
    with open(file_name) as file:
        dict = {}
        for l in file:
            l = l.replace('\n', '')
            l1 = l.split(';')
            if l1[0] == 'id':
                continue
            dict[l1[0]] = l1[1:]
        return dict

def fun(dict):
    for key, value in dict.items():
        for list_index, list_value in enumerate(value):
            value[list_index] = int(list_value)

def grade_points(points):
    grade = -1
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5

def main():
    if True:
        student_file = input('Student information: ')
        exercises_file = input('Exercises completed: ')
        exam_file = input('Exam points: ')
    else:
        student_file = 'students1.csv'
        exercises_file = 'exercises1.csv'
        exam_file = 'exam_points1.csv'
    
    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)
    
    fun(exercises)
    fun(exams)

    for id, name in students.items():
        exercise_points = int(((sum(exercises[id])/40)*100)//10)
        exam_points = sum(exams[id])
        grade = grade_points(exercise_points+exam_points)
        print(f'{name[0]} {name[1]} {grade}')

main()
