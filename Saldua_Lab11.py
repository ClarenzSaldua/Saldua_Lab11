print('Enter the grade of the students (Must only be 40 - 100)')

studentNum = 1 
grades = []
systemLoop = True
total_grade= 0
passedStudentNum = 0

while systemLoop == True:
    studentGrade = input(f'Student #(studentNum): ')
    if studentGrade.replace(".", "",1).isdigit() and studentGrade.count(".") <= 1:
        studentGrade = float(studentGrade)
        if studentGrade >= 40 and studentGrade <= 100:
            grades.append(studentGrade)
            studentNum += 1
            continue
        else:
            print('[Invalid grade] Please enter a number between 40 and 100. ')
            continue
    elif studentGrade.lower() == 'done':
        systemLoop = False
    else:
        print('[Invalid input] Please enter a integer. ')
        continue
else:
    if grades != []:
        for grade in grades:
            total_grade += grade
            averageGrade = total_grade / len(grades)
        else:
            print(f'Average Grade: {averageGrade:.2f}')
        for grade in grades:
                if grade >= 75:
                    passedStudentNum += 1
        else:
            print(f'Number of students Passed :{passedStudentNum}')
            passPercentage = (passedStudentNum / len(grades)) *100
            print(f'Pass Percentage: {passPercentage:.2f}%')
    else:
        print('No grade have been entered.')               
    