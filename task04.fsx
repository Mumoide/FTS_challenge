// Task 4
// Function that splits the input with a custom delimiter
let customSplitString (input: string) =
    let delimiter = (input.Substring(2, input.IndexOf('\n')-2))
    let input = input.Substring(input.IndexOf('\n') + 1)
    // Split the string by comma or by newline.
    let numbers = input.Split(delimiter)
    // Convert the data type of numbers array to be integers by mapping each element to the 'int' function.
    let intNumbers = numbers |> Array.map int
    // Sum the elements of the intNumbers array and return the result.
    Array.sum intNumbers

// Function that splits the input string by commas or by newline and returns an array of integers.
let splitString (input: string) =
    if input.StartsWith("//") then
        customSplitString input
    else
        // Split the string by comma or by newline.
        let numbers = input.Split(',','\n')
        // Convert the data type of numbers array to be integers by mapping each element to the 'int' function.
        let intNumbers = numbers |> Array.map int
        // Sum the elements of the intNumbers array and return the result.
        Array.sum intNumbers


// Function intAdd takes a string as input and returns an integer as output.
let intAdd (string: string) =
    // Creating a try-with block to handle potential exceptions.
    try
        // If the input string is empty, return 0.
        if string = "" then
            0 // If the input string is empty, return 0
        // Otherwise, continue with the execution.
        else
            splitString string
    with
    // First and only pattern to match the exception of this function.
    | :? System.FormatException as ex -> 
    // Prints the message of the exception to the console.
    printfn "%s" ex.Message
    // If the input string is not in the correct format, return 0
    0 
// I have learned that %d is used to print a digit
printfn "%d" (intAdd "//;\n1;2;3") // Output: 6