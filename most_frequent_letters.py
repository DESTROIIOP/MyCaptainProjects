def most_frequent(input_string):
    char_frequency = {}

    for char in input_string:
        if char.isalpha():
            char_frequency[char] = char_frequency.get(char, 0) + 1

    sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)

    for char, frequency in sorted_chars:
        print(f"'{char}': {frequency}")

# Get the input string from the user
user_input = input("Enter a string: ")
most_frequent(user_input)
