# Initialize an empty dictionary to store player names and scores
players = dict()

# Instructions for the user
print("Enter the player's name and score separated by spaces.")
print("Press Ctrl+C to save the data and stop.")

i = 0
while True:
    try:
        # Prompt the user to enter player's first name, last name, and score
        fname, lname, score = input(f"Player {i}: ").split(maxsplit=2)
        
        # Ensure the score is a non-negative integer
        if int(score) < 0:
            raise ValueError
        
        # Add the player's full name and score to the dictionary
        players[fname + " " + lname] = int(score)
        i += 1
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter the player's first name, last name, and total scores separated by spaces.")
    except KeyboardInterrupt:
        # Handle Ctrl+C to save data and stop the loop
        print("\nSaved.")
        break

# Display all players
print("Players are:")
max_score = 0
for name, score in players.items():
    print(f"{name}")

    # Find the player with the highest score
    if score > max_score:
        max_score = score
        best_player_name = name

# Display the player with the highest score
print(f"Player with highest score is: {best_player_name} scoring {max_score}")

# Sort the dictionary by player names in alphabetical order
sorted_dictionary = dict(sorted(players.items(), key=lambda x: x[0]))
print("Players sorted in alphabetical order:")
for name, score in sorted_dictionary.items():
    print(f"{name} -> {score}")

# Display players who have scored 200 or more
print("Players with double centuries:")
for name, score in sorted_dictionary.items():
    if score >= 200:
        print(f"{name} -> {score}")
