# Task 2
def defaultDelimiter(input):
    try:
        return [int(number) for number in input.split(',')]
    except ValueError:
        raise ValueError("Invalid input")
    
    
    
def intAdd(numbers):
    if numbers == "":
        return 0
    number_list = defaultDelimiter(numbers)
    # if len(number_list) > 2:
    #     raise ValueError("Too many numbers")
    return sum(number_list)
    
print(f"{intAdd("1,2,3")}") # Output: 6