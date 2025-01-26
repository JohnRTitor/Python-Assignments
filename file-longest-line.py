# Function to find the longest line in a text file
def find_longest_line(file_path):
    longest_line = ""
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Iterate through each line in the file
            for line in file.readlines():
                # Update longest_line if the current line is longer
                if len(line) > len(longest_line):
                    longest_line = line
    # Handle the case where the file is not found
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    # Handle other I/O errors
    except IOError:
        print(f"Error: An I/O error occurred while accessing the file at {file_path}.")
        return None
    # Return the longest line without leading/trailing whitespace
    return longest_line.strip()

# Prompt the user to enter the path of the text file and strip any surrounding quotes
file_path = input("Enter the path of the text file: ").strip("'\"")
# Find the longest line in the specified file
longest_line = find_longest_line(file_path)
# If a longest line was found, print it
if longest_line:
    print("The longest line is:")
    print(longest_line)
