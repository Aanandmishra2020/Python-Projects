# Welcome Message
print("Welcome To Aanand Mishra's Hypotenuse And Area Calculator App")

# Input from user for Perpendicular And Base
perpendicular = float(input("\nPlease enter length of perpendicular: "))
base = float(input("PLease enter length of base: "))

# Formula For Hypotenuse And Area
hypotenuse = round((perpendicular**2+base**2)**(1/2), 2)
area = round((1/2)*base*perpendicular, 2)

# Printing Hypotenuse And Area
print(f"\nThe hypotenuse of right angled triangle is: {hypotenuse}")
print(f"The area of right angled triangle is: {area}")

# Thanks Message
print("\nThanks, For Using Aanand Mishra's Hypotenuse And Area Calculator App.")
