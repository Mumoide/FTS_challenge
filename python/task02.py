# Task 2
# Function to handle default delimiter by comma 
def defaultDelimiter(input):
    try:
        # Split the input string by comma and convert to integers
        return [int(number) for number in input.split(',')]
    # Reraise ValueError if conversion fails
    except ValueError:
        raise ValueError("Invalid input")
    
    
    
# Function with string input to add numbers
def intAdd(numbers):
    # If input is empty, return 0
    if numbers == "":
        return 0
    # use defaultDelimiter with string input to get list of numbers
    number_list = defaultDelimiter(numbers)
    # Remove the check for more than 2 numbers
    # if len(number_list) > 2:
    #     raise ValueError("Too many numbers")
    # Return the sum of the numbers
    return sum(number_list)
    
print(f"{intAdd("1,2,3")}") # Output: 6