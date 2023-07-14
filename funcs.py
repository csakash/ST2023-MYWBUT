# x = 10
# print(x**2)

# def square_of_a_number(param):
#     result = param**2
#     return result

# x = int(input("Enter a number you want to square: "))
# output = square_of_a_number(param=x)
# print(output)

# y = 3*x**2 + 4*x + 5

def formula(param):
    result = 3*(param**2) + 4*param + 5
    return result

# x = int(input("Enter the parameter: "))
# output = formula(param=x)
# print(output)

def addition(b, a=6):
    return a + b

c = addition(b=7)
print(c)