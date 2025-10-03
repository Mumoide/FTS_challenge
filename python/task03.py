# Task 3
# Function to handle default delimiter by comma and newline
def defaultDelimiter(input):
    try:
        # Transform newlines to comma
        for delimiter in ['\\n']:
            numbers = input.replace(delimiter, ',')
        # Split the input string by comma, convert to integers and return the sum of them
        return sum([int(number) for number in numbers.split(',')])
    # Reraise ValueError if conversion fails
    except ValueError:
        raise ValueError("Invalid input")

# Function with string input to add numbers
def intAdd(numbers):
    # If input is empty, return 0
    if numbers == "":
        return 0
    # Return the sum of the numbers using the defaultDelimiter function
    return defaultDelimiter(numbers)
    
print(f"{intAdd("1,2,3\\n4")}") # Output: 10