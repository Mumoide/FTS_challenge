// Task 1
// I have to create a method to add two numbers contained in a string, where the numbers are separated by a comma.
// In a traditional manner, I would define a method or function that takes a string as input, split the numbers by the comma,
// converts them into integers, and then sums them up.
// But how do I define a method in F#?
// I can use the 'let' keyword to define a function.
// Now I need to know how to define the parameters, which is done by specifying the parameter name and its type in parentheses.
// The return type of the function can be inferred by the compiler, so I don't need to specify it.
let intAdd (string: string) =
    // I will approach this problem as I described above.
    // First, I need to split the string by the comma to get the individual numbers. For this I can use the 'Split' method from the 'String' class.
    let numbers = string.Split(',')
    // 
    // Then, I can convert each number from a string to an integer.
    // For this step, I have to cast each string to an integer, how do I do it in F#?
    // I can use the 'int' function to convert a string to an integer.
    // I have to apply this funciton to each element in the array, this would be a mapping operation.
    // In F#, I can use the 'Array.map' function to apply a function to each element in an array.
    // The operator '|>' is used to pass the result of the left side to the function on the right side, this is called forward pipe operator
    let intNumbers = numbers |> Array.map int
    // Finally, I can sum the integers and return the result using the 'Array.sum' function.
    Array.sum intNumbers

printfn "%d" (intAdd "1,2") // Output: 3