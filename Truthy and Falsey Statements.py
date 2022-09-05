strings = input("Enter any string other than an empty one")

if strings:
    print("Thank you for entering somthing.")
else:
    print("You did not enter a string")

# For integers , 0 is the falsey value. Any integers other than 0 are truthy
# For Floats , 0.0 is the falsey value , Any other floates are truthy

print(bool(2)) # Used to see if the statement is truth or false

