# Task 6
# Exception class for handling negative numbers
class NegativeNumberError(Exception):
        # Constructor with value and message
        def __init__(self, value, message="negatives not allowed"):
            self.value = value
            self.message = message
            # Invoke the base class constructor to set the message of the exception
            super().__init__(f"{self.message}: {self.value}")


# Function to handle default delimiter by comma and newline
def defaultDelimiter(input):
    try:
        # Transform newlines to comma
        for delimiter in ['\\n']:
            numbers = input.replace(delimiter, ',')
        # Create a list of numbers
        numbers = numbers.split(',')
        # Create a list of negative numbers using a filter and lambda function
        negative_numbers = list(filter(lambda x: int(x) < 0, numbers))
        # Check if any negative number exists, if so, raise NegativeNumberError
        if negative_numbers:
            raise NegativeNumberError(negative_numbers)
        # Removing values greater than 1000
        numbers = list(filter(lambda x: int(x) <= 1000, numbers))
        # Return the sum of the list of numbers
        return sum([int(number) for number in numbers])
    # Reraise ValueError if conversion fails
    except ValueError:
        raise ValueError("Invalid input")
    # Catch NegativeNumberError and return the exception
    except NegativeNumberError as e:
        return e
    # Catch any other exceptions
    except Exception as e:
        print("An unknown error ocurred:", e)


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
         # Create a list of numbers
        numbers = numbers.split(',')
        # Create a list of negative numbers using a filter and lambda function
        negative_numbers = list(filter(lambda x: int(x) < 0, numbers))
        # Check if any negative number exists, if so, raise NegativeNumberError
        if negative_numbers:
            raise NegativeNumberError(negative_numbers)
        # Removing values greater than 1000
        numbers = list(filter(lambda x: int(x) <= 1000, numbers))
        # Return the sum of the list of numbers
        return sum([int(number) for number in numbers])
    # Reraise ValueError if conversion fails
    except ValueError:
        raise ValueError("Invalid input")
    # Catch NegativeNumberError and return the exception
    except NegativeNumberError as e:
        return e
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
    
print(f"{intAdd("1,2,3\\n4,2000")}") # Output: 10

# Testing custom delimiter of length 2
print(f"{intAdd("//[xd]\\n1xd2xd3xd4xd2000")}") # Output: 10

# Testing custom delimiter of length 3
print(f"{intAdd("//[-:,]\\n1-:,2-:,3-:,4-:,2000")}") # Output: 10

print(f"{intAdd("1,2,3\\n4,-4,-5")}") # Output: negatives not allowed: ['-4', '-5']