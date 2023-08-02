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


def main():
    name = getValidName("Enter Student's Name Level: ")
    section = validSection("Enter Student's Section: ")
    print()
    print()
    print("STUDENT REPORT")
    print("Student Name:", name)
    print("Student Grade and Section:", section)


if __name__ == "__main__":
    main()
