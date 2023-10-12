def capital_indexes(input_string):
    indexes = []
    
    for index, char in enumerate(input_string):
        if char.isupper():
            indexes.append(index)
    
    return indexes

input_string = input("Enter String: ")
result = capital_indexes(input_string)
print(result)
