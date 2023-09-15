def menu():
    print("=============Menu=============")
    print("____________Main:__________")
    print("Wintermelon = ₱70.00")
    print("Chocolate = ₱50.00")
    print("Strawberry = ₱60.00")
    print("____________Add-on:__________")
    print("Pearl = ₱5.00")
    print("Nata = ₱10.00")
    print("None = ₱0")
    print("=============Menu=============")

def run_program():
    while True:
        menu()
        choices = {'wintermelon': 70, 'chocolate': 50, 'strawberry': 60}
        addons = {'pearl': 5, 'nata': 10, '': 0}
        milk_tea = input("Main: ").lower()
        if milk_tea not in choices:
            print("Invalid Selection! Please try again.")
            continue
        
        milk_tea_add = input("Add-on: ").lower()
        if milk_tea_add not in addons:
            print("Invalid Selection! Please try again.")
            continue
        
        total = choices[milk_tea] + addons[milk_tea_add]
        print(f"Your total is: ₱{total}")
        pay = int(input("Your money is: ₱"))
        balance = pay - total
        if pay < total:
            print("Sorry, you do not have enough balance for the transaction.")
        elif pay >= total:
            print(f"You ordered: {milk_tea} with an add-on of {milk_tea_add}")
            print(f"Your balance is: {balance}")
         
        choice = input("Do you want to continue(Yes or No): ")
        if choice.lower() != "yes":
            print("Thank you for buying our drinks!")
            break
        else:
            continue
        
run_program()
        
    