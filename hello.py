print("Hello World!!")

# This is called a comment in Python. This is a program for writing hello world
"""
    Any multiline comment can be written over here
    This is the second line
"""

# Let's do a simple addition

# 4+5=9
# a = 4
# b = 5
# c = a + b
# x = a - b
# y = a * b
# z = a/b

# print(a+b)
# print(c)
# print(c, x, y, z)
# "A" + "B" =  "AB" "12" + "23" = "1223"

input_a = int(input("Please enter the first number: ")) # this is called typecasting
input_b = int(input("Please enter the second number: "))

result = input_a + input_b

print("This is the first number: ", input_a, type(input_a))
print("This is the second number: ", input_b, type(input_b))
print("Addition is : ", result, type(result))