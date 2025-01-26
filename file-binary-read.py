import pickle

# Function to display trains from Howrah to Jammu
def display_trains_from_howrah_to_jammu(file_path):
    try:
        # Open the binary file in read mode
        with open(file_path, 'rb') as file:
            # Load the list of trains from the binary file
            trains = pickle.load(file)
            print("Trains from Howrah to Jammu are:")
            # Iterate through the list of trains
            for train in trains:
                # Check if the train starts from Howrah and goes to Jammu
                if train['start'] == 'Howrah' and train['destination'] == 'Jammu':
                    # Print the train details
                    print(train)
    # Handle the case where the file is not found
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    # Handle other I/O errors
    except IOError:
        print(f"Error: An I/O error occurred while accessing the file at {file_path}.")

# Example usage
# Prompt the user to enter the path of the binary file and strip any surrounding quotes
file_path = input("Enter the path of the binary file: ").strip("'\"")
# Display the trains from Howrah to Jammu
display_trains_from_howrah_to_jammu(file_path)
