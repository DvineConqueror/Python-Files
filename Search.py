name1 = input("Enter First Name: ")
name2 = input("Enter Second Name: ")
name3 = input("Enter Third Name: ")
name4 = input("Enter Fourth Name: ")
name5 = input("Enter Fifth Name: ")
names = [name1, name2, name3, name4, name5]
print("S for Search and E for End")

choice = input("What do you want to do?: ")

if choice.lower() == 's':
    search = input("Enter name for search: ")
    if search in names:
        print("Name exists")
    else:
        print("Does not exist")
   

if choice.lower() == 'e':
    print("Thank you for using me!")
