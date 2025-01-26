# Prompt the user to enter the path of the text file and strip any surrounding quotes
file_path = input("Enter the path of the text file: ").strip("'\"")

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        print("Lines containing 'Python':")
        # Iterate through each line in the file
        for line in file:
            # Check if the line contains the word 'Python'
            if "Python" in line:
                # Print the line if it contains 'Python'
                print(line)
# Handle the case where the file is not found
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
# Handle other I/O errors
except IOError:
    print(f"Error: An I/O error occurred while accessing the file at {file_path}.")
