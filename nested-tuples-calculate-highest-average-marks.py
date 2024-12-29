# Prompt the user to enter the number of students
count_student = int(input("Enter the number of students: "))

# Initialize an empty tuple to store the marks and average of each student
tup = ()
# Initialize a variable to keep track of the highest average marks
max_avg = 0

# Iterate through each student
for i in range(count_student):
    print("Student", i + 1)
    # Prompt the user to enter the marks for each subject and convert them to integers
    ben_marks = int(input("\tBengali marks: "))
    eng_marks = int(input("\tEnglish marks: "))
    math_marks = int(input("\tMath marks: "))
    phy_marks = int(input("\tPhysics marks: "))
    chem_marks = int(input("\tChemistry marks: "))
    bio_marks = int(input("\tBiology marks: "))

    # Calculate the average marks for the student
    avg_marks = (ben_marks + eng_marks + math_marks + phy_marks + chem_marks + bio_marks) / 6

    # Check if the current student's average marks are higher than the max_avg
    if max_avg < avg_marks:
        # Update max_avg and store the index of the topper
        max_avg = avg_marks
        topper = i

    # Add the student's marks and average to the tuple
    tup = tup + ((ben_marks, eng_marks, math_marks, phy_marks, chem_marks, bio_marks, avg_marks), )

# Print the student with the highest average marks
print("Student with highest average marks:")
print(f"Student {topper} with average marks {max_avg}")
