import cs50

# Get amount of change (positive amount)
while True:
    print("Hi, how much change is owed?")
    totalAmount = cs50.get_float()
    if totalAmount > 0:
        break
    
# Convert change owed to cents    
changeOwed = round(totalAmount * 100)

# Define all the coin values
quarters, dimes, nickels, pennies = 25, 10, 5, 1
totalCoins = 0

# Math to determine least amount of coins possible to return change
while quarters <= changeOwed:
    changeOwed = changeOwed - quarters
    totalCoins += 1

while dimes <= changeOwed:
    changeOwed = changeOwed - dimes
    totalCoins += 1

while nickels <= changeOwed:
    changeOwed = changeOwed - nickels
    totalCoins += 1

while pennies <= changeOwed:
    changeOwed = changeOwed - pennies
    totalCoins += 1

print(totalCoins)