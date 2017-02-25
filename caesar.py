import cs50
import sys

# Verify that a key was given in command line argument
if len(sys.argv) < 2:
    print ("Error: Please enter one command line argument (Number of letters to shift).")
    exit(1)
key = int(sys.argv[1])

# Get the plaintext to be converted
print("plaintext: ", end="")
userInput = cs50.get_string()

# Perform caesar cipher on the plaintext, making sure upper case stays upper, and lower stays lower
for i in range (len(userInput)):
    if (str.isalpha(userInput[i]) and ord(userInput[i]) <= 90):
        print ((chr(((((ord(userInput[i])-65) + key) % 26) + 65))), end="")
        
    elif (str.isalpha(userInput[i]) and ord(userInput[i]) >= 97):
        print ((chr(((((ord(userInput[i])-97) + key) % 26) + 97))), end="")
        
    else:
        print(userInput[i], end="")

# New line for any commands after program finishes
print()