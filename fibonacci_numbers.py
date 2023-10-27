def generate_fibonacci(limit):
    fibonacci_sequence = []
    a, b = 0, 1

    while a < limit:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

# Input: Accept the limit from the user
limit = int(input("Enter the limit for generating Fibonacci numbers: "))

if limit <= 0:
    print("Please enter a positive limit.")
else:
    # Generate and print Fibonacci numbers up to the specified limit
    fibonacci_numbers = generate_fibonacci(limit)
    print("Fibonacci numbers up to", limit, "are:")
    print(fibonacci_numbers)
