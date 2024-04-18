#! python3

"""
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions (not used in this assignment).
Have the user enter in values for a, b and c and then 
tell them if the equation can be factored.

Inputs:
- 3 numbers (a, b, c)

Outputs:
- "the equation can be factored"
- "the equation can not be factored"

Example:
Enter a: 1
Enter b: 4
Enter c: 4
the equation can be factored

Enter a: 1
Enter b: 4
Enter c: 8
the equation can not be factored

"""

a = input("Enter a number => ")
a = int(a)

b = input("Enter a number => ")
b = int(b)

c = input("Enter a number => ")
c = int(c)

t = b**2 - 4 * a * c

if t < 0:
    print("the equation can not be factored")
elif t > 0:
    tt = t**0.5
    rounded = round(tt)
    if rounded == t:
        print("the equation can be factored")

