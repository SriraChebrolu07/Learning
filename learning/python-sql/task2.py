# def vowel(inputlist):
#     vowels = "aeiouAEIOU"
#     result_list = list(filter(lambda word: word[0] in vowels, inputlist))
#     return result

# inputlist = ["armagedon", "ballentines", "opera", "knot", "great", "pearl"]
# result = vowel(inputlist)
# print(result)



# strings=["lucifermorningstar", "lucy", "Interstellar", "kingsman"]

# longwords= list(filter(lambda a: len(a)>5,strings))
# print(longwords)

# def longwords(a):
#     return len(a)>5

# strings=["lucifermorningstar", "lucy", "Interstellar", "kingsman"]
# result= list(filter(longwords,strings))
# print(result)



def calculate_average(grades):
    # Calculate the average grade for each student
    averages = []
    for student in grades:
        name = student[0]  # Extract the student's name from the tuple
        grades_sum = sum(student[1])  # Calculate the sum of grades using the sum function
        average = grades_sum / len(student[1])  # Calculate the average by dividing the sum by the number of grades
        averages.append((name, average))  # Append a tuple containing the student's name and average grade to the list
    return tuple(averages)  # Convert the list of tuples to a tuple and return

# Example usage
students_grades = (
    ('Alice', (90, 85, 92)),
    ('Bob', (88, 76, 80)),
    ('Charlie', (95, 89, 94)),
)

result = calculate_average(students_grades)
print(result)


def calculate_average(grades):
    # Calculate the average grade for each student
    averages = []
    for student in grades:
        name = student[0]
        grades_sum = sum(student[1])
        average = grades_sum / len(student[1])
        averages.append((name, average))
    return tuple(averages)

# Example usage
studentsgrades = (
    ('Ankit', (89, 95, 99)),
    ('vikram', (91, 79, 95)),
    ('sunil', (85, 89, 88)),
)

result = calculate_average(studentsgrades)
print(result)
