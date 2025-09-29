// Task 8
// Defining a new Exception type for handling negative numbers
exception NegativeNumberException of string

// Function that returns all the custom delimiters as a tuple
let customDelimiters(input: string) =
    // Replaces the closing brackets with empty strings, then splits the string by the opening brackets
    input.Replace("]","").Split('[')

// Function that removes numbers greater than 1000
let removeBigNumbers(numbers: int array) =
    // Filters the input array, returning only numbers lesser than or equal to 1000
    numbers |> Array.filter (fun x -> x <= 1000)

// Function that raises an exception when a negative number is found in the array of numbers
let raiseIfNegative (numbers: int array) =
    // Declaring a match expression to compare the result of the input array after applying a filter that checks if a number is lesser than 0.
    match numbers |> Array.filter (fun x -> x < 0) with
    // Pattern matching that checks if the array is empty
    | [||] -> ()
    // Pattern matching, using the wildcard to raise an error with a custom message when the array has a value
    | values -> raise (NegativeNumberException (sprintf  "negatives not allowed: %s" (String.concat ", " (Array.map string values))))

// Function that splits the input with a custom delimiter
let customSplitString (input: string) =
    // Extracting the custom delimiter starting after '//' and ending before the first newline character '\n'.
    // For this the method IndexOf was used to find the index of the first newline character '\n'.
    // The method Substring was used to extract the custom delimiter.
    // The customDelimiters function is used to get all the custom delimiters as an array of strings.
    let delimiter = customDelimiters(input.Substring(2, input.IndexOf('\n') - 2))
    // Substring is used to extract the string that will be processed, this is the substring after the custom delimiter definition.
    let input = input.Substring(input.IndexOf('\n') + 1)
    // Split the string by the custom delimiter.
    let numbers = input.Split(delimiter, System.StringSplitOptions.RemoveEmptyEntries)
    // Convert the data type of numbers array to be integers by mapping each element to the 'int' function.
    let intNumbers = numbers |> Array.map int
    // Raise an exception if any negative numbers are found
    raiseIfNegative (intNumbers)
    // Sum the numbers lesser lesser or equal than 1000 of the intNumbers array and return the result.
    Array.sum (removeBigNumbers(intNumbers))

// Function that splits the input string by commas or by newline and returns an array of integers.
let defaultSplitString(input: string) =
    // Split the string by comma or by newline.
    let numbers = input.Split(',','\n')
    // Convert the data type of numbers array to be integers by mapping each element to the 'int' function.
    let intNumbers = input.Split(',','\n') |> Array.map int
    // Raise an exception if any negative numbers are found
    raiseIfNegative (intNumbers)
    // Sum the numbers lesser lesser or equal than 1000 of the intNumbers array and return the result.
    Array.sum (removeBigNumbers(intNumbers))

// Function splits the input dynamically, being able to handle custom delimiters or default delimiters.
let splitString (input: string) =
    // Matching expression to choose between custom or default splitting
    match input with
    // The following line uses guard on pattern, it uses the 'when' keyword to specify an additional condition that must be satisfied.
    // In this case, the first two characters must be equal to '//', if that is true, then the string is passes to the custom splitting method
    | string when string.StartsWith("//")  -> customSplitString string
    // Otherwise it passes the input to the default splitting method
    | string -> defaultSplitString string

        
// Function intAdd takes a string as input and returns an integer as output.
let intAdd (string: string) =
    // Creating a try-with block to handle potential exceptions.
    try
        // If sentence was changed with a match expression. It compares a string with the declared options
        match string with
        // When string is empty or null, then returns 0. This is a constant pattern.
        | "" | null -> 0
        // '_' is used as a wildcard, its used as the last pattern to match any previously unmatched input values.
        | _ -> splitString string
    with
    // First and only pattern to match the exception of this function.
    | :? System.FormatException as ex -> 
        // Prints the message of the exception to the console.
        printfn "%s" ex.Message
        // If the input string is not in the correct format, return 0
        0 
    | :? NegativeNumberException as ex ->
        // Prints the message of the exception to the console.
        printfn "%s" ex.Message
        0

// Adding numbers with a custom delimiter
printfn "Custom delimiter: %d" (intAdd "//[;]\n1;2;3") // Output: 6

// Adding numbers with a custom delimiter of length equal to 2
printfn "Custom delimiter of length 2: %d" (intAdd "//[;.]\n5;.5;.5") // Output: 15

// Adding numbers with a custom delimiter of length equal to 4
printfn "Custom delimiter of length 4: %d" (intAdd "//[;.:-]\n10;.:-5;.:-2") // Output: 17

// Adding numbers with multiple custom delimiter of different lengths
printfn "Multiple custom delimiter of different lengths: %d" (intAdd "//[;.:-][;-]\n10;.:-5;.:-2;-5;-3") // Output: 25

// Adding numbers with default delimiters (only comma)
printfn "Default delimiter: %d" (intAdd "1,2,3,-4") // Exception is raised and 0 is returned

// Adding numbers with default delimiters (comma and newline)
printfn "Default delimiter (Comma and newline): %d" (intAdd "1\n2,3") // Output: 6

// Adding numbers with default delimiters (only comma) and numbers greater than 1000
printfn "Default delimiter with numbers greater than 1000: %d" (intAdd "1,2,3,4,1001") // Output: 10