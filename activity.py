def getValidName(prompt):
    while True:
        try:
            name = input(prompt)
            if not any(char.isalpha() for char in name):
                raise ValueError("Invalid input. Please input your name!")
            return name
        except ValueError as ve:
            print(ve)


def validSection(prompt):
    while True:
        try:
            name = input(prompt)
            if not any(char.isalpha() for char in name):
                raise ValueError("Invalid input. Please input your section!")
            return name
        except ValueError as ve:
            print(ve)


def validGradeLevel(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter your grade.")


def validQuarterGrade(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid float value.")


def main():
    name = getValidName("Enter Student's Name Level: ")
    gradeLevel = validGradeLevel("Enter Student's Grade Level: ")
    section = validSection("Enter Student's Section: ")
    print()
    firstQuarter = validQuarterGrade("Enter Student's First Quarter Grade: ")
    secondQuarter = validQuarterGrade("Enter Student's Second Quarter Grade: ")
    thirdQuarter = validQuarterGrade("Enter Student's Third Quarter Grade: ")
    fourthQuarter = validQuarterGrade("Enter Student's Fourth Quarter Grade: ")
    print()
    print("STUDENT REPORT")
    print("Student Name:", name)
    print("Student Grade and Section:", str(gradeLevel) + "-" + section)
    print(" Grades:\n      First Quarter:", firstQuarter, "\n      Second Quarter:", secondQuarter,
          "\n      Third Quarter:", thirdQuarter, "\n      Fourth Quarter:", fourthQuarter)


if __name__ == "__main__":
    main()
