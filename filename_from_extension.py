# Input: Accept the file name from the user
file_name = input("Enter a file name: ")

# Split the file name into parts using the period (.) as a delimiter
parts = file_name.split(".")

# Check if there is at least one period in the file name
if len(parts) > 1:
    # The extension is the last part of the split result
    extension = parts[-1]
    print(f"The file extension is: {extension}")
else:
    print("The file name doesn't have an extension or is not a valid file name.")
