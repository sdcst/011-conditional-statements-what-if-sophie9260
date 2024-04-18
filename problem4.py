#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


3, 4, 5.2
expected hypotenuse = 5
2% of 5 is 0.1
smallest acceptable number = 4.9
largest acceptable number = 5.1

if 4.9 < 5 < 5.1 then it is right triangle
if 5 > 5.1 then obtuse
if 5 < 4.9 acute

"""
n = input("Enter a number ")
n = float(n)

nn = input("Enter another number ")
nn = float(nn)

nnn = input("Enter another number ")
nnn = float(nnn)

h = max(n,nn,nnn)

a = min(n,nn,nnn)

t = n + nn + nnn
tt = a + h
b = t - tt

c = (a**2 + b**2)**0.5

maxh = c*1.02
minh = c - (c*0.02)

if minh < h < maxh:
    print("that is a right triangle")
elif h > maxh:
    print("that is an obtuse triangle")
elif h < minh:
    print("that is an acute triangle")
