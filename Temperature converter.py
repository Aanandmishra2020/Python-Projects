# Welcome Message
print("Welcome To Aanand Mishra's Temperature Converter App")

# Input Fahrenheit
fahrenheit = float(input("\nPlease enter the temperature(in fahrenheit): "))

# Converting Into Celsius
celsius = round((fahrenheit-32)*5/9,2)

# Converting Into Kelvin
kelvin = round(((fahrenheit-32)*5/9)+273.15,2)

# Printing Celsius And Kelvin Value
print(f"\nIn Celsius: {celsius}")

# Printing Kelvin Value
print(f"\nIn Kelvin: {kelvin}k")

# Thanks Message
print("\nThanks, For Using Aanand Mishra's Temperature Converter App.")
