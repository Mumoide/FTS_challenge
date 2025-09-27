// Task 1
// I have to create a method to add two numbers contained in a string, where the numbers are separated by a comma.
// In a traditional manner, I would define a method or function that takes a string as input, split the numbers by the comma,
// converts them into integers, and then sums them up.
// But how do I define a method in F#?
// I can use the 'let' keyword to define a function.
// Now I need to define the parameters, which is done by specifying the parameter name and its type in parentheses.
// The return type of the function can be inferred by the compiler, so I don't need to specify it.
let intAdd (string: string) =
    // First, I need to split the string by the comma to get the individual numbers.
    let numbers = string.Split(',')
    // Then, I can convert each number from a string to an integer.
    let intNumbers = numbers |> Array.map int
    // Finally, I can sum the integers and return the result.
    Array.sum intNumbers

printfn "%d" (intAdd "1,2") // Output: 3