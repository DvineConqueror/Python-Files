price = float(input("Enter Price: "))
quantity = float(input("Enter Quantity: "))

total = price * quantity
print(f"Total Payable: {total}")

if total >= 1000:
    discount = total / 10
    new_total = total - discount
    print("10% discount available!")
    print(f"Amount Payable: {new_total}")
    
elif total >= 500:
    discount = total / (100 / 5)
    new_total = total - discount
    print("5% discount available!")
    print(f"Amount Payable: {new_total}")
    
else:
    print("Invalid Input")