# Task 4
def defaultDelimiter(input):
    try:
        for delimiter in ['\\n']:
            numbers = input.replace(delimiter, ',')
        return sum([int(number) for number in input.split(',')])
    except ValueError:
        raise ValueError("Invalid input")

def customDelimiter(input):
    try:
        delimiter, numbers = input.split('\\n', 1)
        delimiter = delimiter[2::]
        delimiter = delimiter.replace("[","").replace("]","")
        for delim in [delimiter]:
            numbers = numbers.replace(delim, ',')
        return sum([int(number) for number in numbers.split(',')])
    except ValueError:
        raise ValueError("Invalid input")
    except Exception as e:
        print("An unknown error ocurred:", e)


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