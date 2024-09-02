# def calgrade(marks):
#     percentage = sum(marks) / len(marks)
#     if percentage >= 90:
#         return "S"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "F"

# marks = []
# for i in range(6):
#     marks.append(float(input(f"Enter marks for subject {i+1}: ")))

# percentage = sum(marks) / len(marks)
# grade = calgrade(marks)

# print(f"Percentage: {percentage:.2f}%")
# print("Grade: ",grade)
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Taking input for 6 subjects
marks_input = input("Enter marks for 6 subjects separated by space: ")
marks = [float(mark) for mark in marks_input.split()]

total_marks = float(input("Enter total marks for all subjects: "))
percentage = (sum(marks) / total_marks) * 100
grade = calculate_grade(percentage)

print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
