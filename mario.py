import cs50

# Get the height of the pyramid between 0 and 23
while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if height in range (0, 23):
        break
       
row = 0
numSpaces = height

# Print the pyramid, making sure top is 2 characters wide
for i in range (height):
    print(" " * (numSpaces-1), end="")
    print("#" * (row+2))
    row += 1
    numSpaces -= 1