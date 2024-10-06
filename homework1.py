# Create the .txt file with a number
number = 200
with open('number.txt', 'w') as file:
    file.write(str(number))  

# Read the number from the file
with open('number.txt', 'r') as file:
    number = int(file.read().strip())

# Calculate the number of decades
decades = number / 10

# Print the result
print(f"The number of decades corresponding to {number} years is: {decades}")
