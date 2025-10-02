# Task 4
class NegativeNumberError(Exception):
        def __init__(self, value, message="negatives not allowed: "):
            self.value = value
            self.message = message
            super().__init__(f"{self.message}: {self.value}")


def defaultDelimiter(input):
    try:
        for delimiter in ['\\n']:
            numbers = input.replace(delimiter, ',')
        numbers = numbers.split(',')
        negative_numbers = list(filter(lambda x: int(x) < 0, numbers))
        if negative_numbers:
            raise NegativeNumberError(negative_numbers)
        return sum([int(number) for number in numbers])
    except ValueError:
        raise ValueError("Invalid input")
    except NegativeNumberError as e:
        return e
    except Exception as e:
        return ("An unknown error ocurred:", e)


def customDelimiter(input):
    try:
        delimiter, numbers = input.split('\\n', 1)
        delimiter = delimiter[2::]
        delimiter = delimiter.replace("[","").replace("]","")
        for delim in [delimiter]:
            numbers = numbers.replace(delim, ',')
        numbers = numbers.split(',')
        negative_numbers = list(filter(lambda x: int(x) < 0, numbers))
        if negative_numbers:
            raise NegativeNumberError(negative_numbers)
        return sum([int(number) for number in numbers])
    except ValueError:
        raise ValueError("Invalid input")
    except NegativeNumberError as e:
        return e
    except Exception as e:
        return ("An unknown error ocurred:", e)


def intAdd(numbers):
    if numbers == "":
        return 0
    if numbers[:2] == "//":
        return customDelimiter(numbers)
    for delimiter in ['\\n']:
        numbers = numbers.replace(delimiter, ',')

    return defaultDelimiter(numbers)
    
print(f"{intAdd("1,2,3\\n4")}") # Output: 10

print(f"{intAdd("//[xd]\\n1xd2xd3xd4")}") # Output: 10

print(f"{intAdd("1,2,3\\n4,-4")}") # Error