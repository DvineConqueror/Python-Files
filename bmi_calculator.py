from pyfiglet import figlet_format
import time

print(figlet_format("Dominic's BMI Calculator !", font="standard"))
print("Below 18.5 = Underweight \n18.5 - 24.9 = Normal \n 25.0 - 29.9 = Overweight \n 30.0+ = Obese")


def weightClass(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 24.9:
        return "Normal"
    elif 25.0 < bmi <= 29.9:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    else:
        return "Error"


while True:
    print("Please select the number of the following: ")
    print("1. Kilogram and Meters | 2. Kilogram and Centimeter | 3. Pounds and Feet |  4. Exit")

    try:
        option = int(input("Input Option: "))
        match option:
            case 1:
                kg = int(input("Enter your Weight (Kg): "))
                meter = float(input("Enter your Height (Meters): "))
                bmi = kg / meter ** 2
                print(f"Body Mass Index: {bmi}")
                print(f"BMI Weight Class: {weightClass(bmi)}")
            case 2:
                kg = int(input("Enter your Weight (Kg): "))
                cMeter = float(input("Enter your Height (Centimeter): "))
                bmi = (kg / (cMeter / 100) ** 2)
                print(f"Body Mass Index: {bmi}")
                print(f"BMI Weight Class: {weightClass(bmi)}")
            case 3:
                lb = float(input("Enter your Weight (lb): "))
                feet = int(input("Enter your Height (Ft): "))
                inch = int(input("Enter your Height (Inch): "))
                heightinInch= (feet * 12) + inch
                bmi = (lb / (heightinInch ** 2)) * 703
                print(f"Body Mass Index: {bmi}")
                print(f"BMI Weight Class: {weightClass(bmi)}")
            case 4:
                print("Thank your for using this program!")
                time.sleep(1.5)
                print("Program Exiting......")
                break
            case _:
                print("Invalid choice! Please select a number from 1 to 4")
                continue

        choice = input("Do you want to continue? Yes or No: ")
        if choice.lower() not in ["yes", "y"]:
            print("Thank your for using this program!")
            time.sleep(1.5)
            print("Program Exiting......")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
