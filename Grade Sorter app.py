# Welcome Message
print("Welcome to the grade sorter app")

# Taking Input
grade = []
grade.append(int(input("\nPlease Enter Your Grade:")))
grade.append(int(input("Please Enter Your Grade:")))
grade.append(int(input("Please Enter Your Grade:")))
grade.append(int(input("Please Enter Your Grade:")))

# Displaying List
print("\nYour grades are "+str(grade))

# Sorting Grades
grade.sort(reverse=True)

# Displaying Sorted List
print("\nYour grades from highest to lowest are: "+str(grade))

# Displaying Lowest And Highest Grades
grade1 = grade[-1]
print("\nLowest grade: "+str(grade1))
grade2 = grade[0]
print("Highest grade: "+str(grade2))

# Deleting Lowest Two Grades
del grade[-1]
del grade[-2]

# Printing Remaining Grades
print(f"\nRemaining grades in list: {grade}")

# Thanks Message
print("\nThanks, For Using Aanand Mishra's Any Letter Counting App.")
