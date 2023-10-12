#Using the nested if statement, create a program that accepts the following information:
#Employee's first name, last name, salaray, and performance rating then calculates the employee's
#end of year bonus. Bonus is calculated based on the employee's annual salary and performance rating. 
#Rating: 1 Bonus = 10%. R 2 Bonus = 6%. R 3 Bonus = 3%. R 4 Bonus = 0

firstName = input("First Name: ")
lastName = input("Last Name: ")
salary = int(input("Salary: "))
rating = int(input("Rating: "))


if salary > 0:
    if rating == 1:
        bonus = (salary//100)*10
    elif rating == 2:
        bonus = (salary//100)*6
    elif rating == 3:
        bonus = (salary//100)*3
    elif rating >= 4:
        bonus = "None"
    else:
        print("Invalid")
    
    print(f"Name: {firstName} {lastName}")
    print(f"Salary: {salary}")
    print(f"Rating: {rating}")
    print(f"Bonus: {bonus}")    
else:   print("Invalid Salary")
        