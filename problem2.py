#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

n = input("Enter a number => ")
n = float(n)

m = round(n)

if n >= 0 and n == m:
    print("The number is an integer.")
else:
    print("The number is not an integer.")