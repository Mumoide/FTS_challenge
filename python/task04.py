# Task 4
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

# Function to handle custom delimiter
def customDelimiter(input):
    try:
        # Split the input by the first newline to separate delimiter and numbers
        delimiter, numbers = input.split('\\n', 1)
        # Extract the actual delimiter by removing the leading '//'
        delimiter = delimiter[2::]
        # Remove brackets if present
        delimiter = delimiter.replace("[","").replace("]","")
        # Replace custom delimiter with comma
        for delim in [delimiter]:
            numbers = numbers.replace(delim, ',')
         # Split the input string by comma, convert to integers and return the sum of them   
        return sum([int(number) for number in numbers.split(',')])
    # Reraise ValueError if conversion fails
    except ValueError:
        raise ValueError("Invalid input")
    # Catch any other exceptions
    except Exception as e:
        print("An unknown error ocurred:", e)


# Function with string input to add numbers
def intAdd(numbers):
    # If input is empty, return 0
    if numbers == "":
        return 0
    # Check if the input starts with '//', if so, use customDelimiter
    if numbers[:2] == "//":
        return customDelimiter(numbers)

    # Otherwise, use defaultDelimiter
    return defaultDelimiter(numbers)
    
print(f"{intAdd("1,2,3\\n4")}") # Output: 10

print(f"{intAdd("//[xd]\\n1xd2xd3xd4")}") # Output: 10