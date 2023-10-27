# Get user input for the range elements
input_str = input("Enter a list of distinct elements separated by spaces: ")
user_input = input_str.split()

# Convert the user input to a list of integers
range_elements = [int(x) for x in user_input]

# Ensure all elements in the list are distinct
if len(set(range_elements)) != len(range_elements):
    print("Please enter distinct elements.")
else:
    # Print all positive numbers in the list
    print("Positive numbers from the user input:")
    for num in range_elements:
        if num > 0:
            print(num)


