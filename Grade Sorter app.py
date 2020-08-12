# Welcome Message
print("Welcome to the grade sorter app")

# Taking Input
grade = []
grade.append(int(input("\nPlease Enter Your First Grade:")))
grade.append(int(input("Please Enter Your Second Grade:")))
grade.append(int(input("Please Enter Your Third Grade:")))
grade.append(int(input("Please Enter Your Fourth Grade:")))
grade.append(int(input("Please Enter Your Fifth Grade:")))

# Displaying List
print("\nYour grades are "+str(grade))

# Sorting Grades
grade.sort(reverse=True)

# Displaying Sorted List
print("\nYour grades from highest to lowest are: "+str(grade))

# Displaying Lowest And Highest Grades
lowest_grade = grade[-1]
print("\nLowest grade: "+str(lowest_grade))
highest_grade = grade[0]
print("Highest grade: "+str(highest_grade))

# Deleting Lowest Two Grades
del grade[-1]
del grade[-2]

# Printing Remaining Grades
print(f"\nRemaining grades in list: {grade}")

# Thanks Message
print("\nThanks, For Using Aanand Mishra's Any Letter Counting App.")
