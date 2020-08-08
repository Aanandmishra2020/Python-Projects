# Welcome Message
print("Welcome to the Any Letter Counting App")

# Input Name
name = input("\nPlease Enter Your Name Here:").title().strip()
print(f"Hello! {name}")

# Input Message
message = input("\nPlease Enter Your Message Here:").lower()

# Input Letter
letter = input("\nPlease Enter The Letter That You Would Like Count:").lower()

# Counting Letters
letter_count = message.count(letter)
print(f"\nThere are {letter_count}'s {letter} in your message.")

# Thanks Message
print("\nThanks, For Using Aanand Mishra's Any Letter Counting App.")
