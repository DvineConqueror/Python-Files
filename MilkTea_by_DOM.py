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
        milk_tea = input("Main: ")
        milk_tea_add = input("Add-on: ")
        
        prices = {'wintermelon': 70, 'chocolate': 50, 'strawberry': 60, 'pearl': 5, 'nata': 10, '': 0}
        total = prices[milk_tea] + prices[milk_tea_add]
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
        
    