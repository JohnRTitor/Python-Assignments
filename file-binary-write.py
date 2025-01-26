import pickle

# Function to get student data from user input
def get_student_data():
    student_data = dict()

    print("Enter the student's first name, last name, and total marks separated by spaces.")
    print("Press Ctrl+C to save the data and stop.")
    i = 0
    while True:
        try:
            # Get student details from user input
            fname, lname, total_marks = input(f"Student {i}: ").split(maxsplit=2)
            # Store the student data in the dictionary
            student_data[fname + " " + lname] = int(total_marks)
            i += 1
        except ValueError:
            print("Invalid input. Please enter the student's first name, last name, and total marks separated by spaces.")
        except KeyboardInterrupt:
            print("\nSaved.")
            break
    return student_data

# Function to get toppers from the student data
def get_toppers(student_data):
    toppers = dict()
    for name, total_marks in student_data.items():
        # Check if the student's total marks are greater than 500
        if total_marks > 500:
            toppers[name] = total_marks
    return toppers

# Prompt the user to enter the path of the text file and strip any surrounding quotes
file_path = input("Enter the path of the text file: ").strip("'\"")
try:
    # Open the file in write-binary mode and save the student data
    with open(file_path, 'wb') as file:
        pickle.dump(get_student_data(), file)
        print("Data saved to file.")

    # Open the file in read-binary mode and load the student data
    with open(file_path, 'rb') as file:
        student_data = pickle.load(file)
        # Get the toppers from the student data
        toppers = get_toppers(student_data)
        print("Toppers:")
        # Print the toppers
        for name, total_marks in toppers.items():
            print(f"{name}: {total_marks} marks")
# Handle the case where the file is not found
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
# Handle other I/O errors
except IOError:
    print(f"Error: An I/O error occurred while accessing the file at {file_path}.")
