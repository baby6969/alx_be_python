# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern using while and for loops
while row < size:
    for col in range(size):
        print("*", end="")  # print stars on the same line
    print()  # move to the next line after a row is complete
    row += 1
