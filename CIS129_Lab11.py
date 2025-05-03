#Isabella Fox
#Lab 11
#Grade tracker in a txt file - 9.1

import csv
from itertools import count

with open('grades.txt', mode='w') as grades:
    while True:
        grades_input = input("Enter class grade here (Reply with 'N/A' to complete program) ")
        if grades_input == 'N/A':   #input to end the program
            break
        if grades_input.isdigit() == True:
            grades.write(grades_input + '\n')
        else:
            print('Enter a non-negative integer.')

#Read grades from grades.txt and display individual grades, total, count and average.
total = 0 #define variable and set to zero
count = 0

with open('grades.txt', 'r') as display:
    for line in display: #Display individual grades and calculate totals/counts
        grade = int(line.strip())
        print(f'Grade: {grade}')
        total += grade
        count += 1

if count > 0:
    average = total/count
    print(f'Total: {total}')
    print(f'Count: {count}')
    print(f'Average: {average}')
else: print('Text file was empty')

#Writing student records to CSV file

with open('grades.csv', mode = 'w',newline='') as student_records:
    csv_file = csv.writer(student_records)

    while True:
        first_name = input("Student's first name: ")
        if first_name == 'N/A':
            break   #stops program
        last_name = input("Student's last name: ")
        try:
            exam1grade = int(input("Exam 1 grade: "))
            exam2grade = int(input("Exam 2 grade: "))
            exam3grade = int(input("Exam 3 grade: "))
        except ValueError:
            print('Incorrect format. Re-input grades')
            continue  #needed to avoid program crashing due to error

        csv_file.writerow([first_name, last_name, exam1grade, exam2grade, exam3grade])
