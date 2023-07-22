import numpy as np

# x = np.array([[3, 4], [7, 6]], dtype=np.float64)
# y = np.array([[1, 2], [3, 2]], dtype=np.float64)

# print("First Element: ")
# print(x)

# print("Second Element: ")
# print(y)

# print("Addition: ")
# print(x+y)

# print(np.add(x, y))

# print("Subtraction: ")
# print(x-y)
# print(np.subtract(x, y))

# print("Multiplication: ")
# print(x*y)
# print(np.multiply(x, y))

# print("Division: ")
# print(x/y)
# print(np.divide(x, y))

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

print(v.dot(x))
print(np.dot(v, x))

print("original matrix: ", x)
print("Transpose of a matrix", x.T)

print("Sum of all the elements: ", np.sum(x))
print("Column wise sum: ", np.sum(x, axis=0))
print("Row wise sum: ", np.sum(x, axis=1))
