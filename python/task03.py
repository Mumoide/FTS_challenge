# Task 3
def defaultDelimiter(input):
    try:
        return [int(number) for number in input.split(',')]
    except ValueError:
        raise ValueError("Invalid input")

def intAdd(numbers):
    if numbers == "":
        return 0
    for delimiter in ['\\n']:
        numbers = numbers.replace(delimiter, ',')

    return sum([int(number) for number in numbers.split(',')])
    
print(f"{intAdd("1,2,3\\n4")}") # Output: 10