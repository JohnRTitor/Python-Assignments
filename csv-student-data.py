import csv

def write_student_data(file_path):
    try:
        # Open the file in write mode
        file = open(file_path, mode='w', newline='')
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["Name", "Roll", "Avg Marks"])

        print("Enter the student's first name, last name, roll and avg marks separated by spaces.")
        print("Press Ctrl+C to save the data and stop.")
        i = 0
        while True:
            try:
                # Read student data from input
                fname, lname, roll, avg_marks = input(f"Student {i}: ").split(maxsplit=3)
                # Write the student data to the CSV file
                writer.writerow([fname + " " + lname, int(roll), int(avg_marks)])
                i += 1
            except ValueError:
                # Handle invalid input
                print("Invalid input. Please enter the student's first name, last name, roll and total marks separated by spaces.")
            except KeyboardInterrupt:
                # Handle Ctrl+C to stop input and save data
                print(f"\nSaved in {file_path}.")
                break
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        # Handle I/O error
        print(f"Error: An I/O error occurred while accessing the file at {file_path}.")
    finally:
        # Close the file
        file.close()

def display_student_data(file_path):
    try:
        # Open the file in read mode
        file = open(file_path, mode='r', newline='')
        reader = csv.reader(file)
        # Read and print each row from the CSV file
        for row in reader:
            print(row)
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        # Handle I/O error
        print(f"Error: An I/O error occurred while accessing the file at {file_path}.")
    finally:
        # Close the file
        file.close()

# Get the file path from the user
file_path = input("Enter the path of the csv file: ").strip("'\"")
# Write student data to the CSV file
write_student_data(file_path)
# Display student data from the CSV file
display_student_data(file_path)
