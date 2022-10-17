project_score = float(input("Please enter your project score percentage: "))
exam_score = float(input("Please enter your exam score percentage: "))

final_grade = (project_score + exam_score) * 0.5

def letter_grade():
    if final_grade >= 80:
        return "A"
    elif final_grade >= 70:
        return "B"
    elif final_grade >= 60:
        return "C"
    elif final_grade >= 50:
        return "D"
    else:
        return "E"

print("Your final grade is " + str(final_grade) + "% in total.")
print("Your corresponding letter grade is " + letter_grade() + ".")