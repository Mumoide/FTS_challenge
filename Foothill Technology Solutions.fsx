// Task 1
// Function intAdd takes a string as input and returns an integer as output.
let intAdd (string: string) =
    // Creating a try-with block to handle potential exceptions.
    try
        // If the input string is empty, return 0.
        if 
            string = "" then 0 // If the input string is empty, return 0
        // Otherwise, continue with the execution.
        else
            // Split the input string by commas to get an array of numbers in string format.
            let numbers = string.Split(',')
            // After splitting, check if the length of the numbers array is greater than 2.
            if numbers.Length > 2 then 
                // If there are more than two elements, raise a FormatException with a custom message.
                raise (System.FormatException("A maximum of two elements is allowed"))
            else
                // Convert the data type of numbers array to be integers by mapping each element to the 'int' function.
                let intNumbers = numbers |> Array.map int
                // Sum the elements of the intNumbers array and return the result.
                Array.sum intNumbers
    with
    // First and only pattern to match the exception of this function.
    | :? System.FormatException as ex -> 
    // Prints the message of the exception to the console.
    printfn "%s" ex.Message
    // If the input string is not in the correct format, return 0
    0 

printfn "%d" (intAdd "1,2") // Output: 3