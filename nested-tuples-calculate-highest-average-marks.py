count_student = int(input("Enter the number of students: "))

tup = ()
max_avg = 0

for i in range(count_student):
    print("Student", i + 1)
    ben_marks = int(input("\tBengali marks: "))
    eng_marks = int(input("\tEnglish marks: "))
    math_marks = int(input("\tMath marks: "))
    phy_marks = int(input("\tPhysics marks: "))
    chem_marks = int(input("\tChemistry marks: "))
    bio_marks = int(input("\tBiology marks: "))

    avg_marks = (ben_marks + eng_marks + math_marks + phy_marks + chem_marks + bio_marks) / 6

    if max_avg < avg_marks:
        max_avg = avg_marks
        topper = i

    tup = tup + ((ben_marks, eng_marks, math_marks, phy_marks, chem_marks, bio_marks, avg_marks), )

print("Student with highest average marks:")
print(f"Student {topper} with average marks {max_avg}")
