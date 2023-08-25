# Import the random module
import random

# Define a function to generate a strong password
def generate_password():
  # Ask the user for the length of the password
  length = int(input("Enter the length of the password: "))
  # Check if the length is valid
  if length < 8 or length > 32:
    print("Invalid length. Please enter a number between 8 and 32.")
    return
  # Define the characters to use in the password
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  digits = "0123456789"
  symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
  # Create an empty password string
  password = ""
  # Loop until the password is of the desired length
  while len(password) < length:
    # Choose a random character type
    char_type = random.choice([lower, upper, digits, symbols])
    # Choose a random character from the type
    char = random.choice(char_type)
    # Append the character to the password string
    password += char
  # Return the password string
  return password

# Call the function and print the result
print("Your strong password is:", generate_password())
