#! python3

# Have the user enter a number 

# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

question = "Enter a number."
n = input(question)
n = float(n)

even = n/2
even = round(even)

if n == even*2:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")


