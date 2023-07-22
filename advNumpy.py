import numpy as np

# arr = np.array([1, 2, 4])
# print(arr)

# arr2d = np.array([
#     [2, 4, 5],
#     [5, 6, 7]
# ])

# print(arr2d)
# print(arr2d.shape)
# print(len(arr2d))

# # Create an array of all zeros

# zeros = np.zeros((5, 5))
# print(zeros, zeros.shape)

# # Create an array of all ones
# ones = np.ones((4, 6))
# print(ones, ones.shape)

# Create a random array of values

# random = np.random.random((5, 5))
# print(random)

# #extract 1st row all columns
# print(random[1:3, 2:5])

# new_arr = random[1:3, 2:5]
# print(new_arr)

# Boolean indexing

# temp = np.array([
#     [3, 4, 5, 6],
#     [8, 5, 7, 3],
#     [1, 5, 8, 3]
# ])

# print(temp)

# Find the elements of an array which are
# bigger than 3
# filtered_idx = (temp > 3)
# print(filtered_idx)
# print(temp[filtered_idx])

# print(temp[temp > 5])


# ARRAY BROADCASTING

# x = np.array([
#     [2, 5, 6],
#     [6, 4, 3],
#     [5, 4, 3]
# ])

# y = np.array([1, 2, 3])

"""
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
"""

# z = np.empty_like(x)
# print(z)

# for i in range(len(x)):
# 	# [0, 0, 0] <- [2, 5, 6] + [1, 2, 3] # at iteration 1
# 	# [3, 7, 9]
# 	# [7, 6, 6]
# 	# [6, 6, 6]
# 	z[i, :] = x[i, :] + y

"""
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
"""

# print(x+y)

# 3*1 , 1*3-> 3*3
# arr = np.tile(y, (3, 1))
# print(arr)


arr = np.array([3, 5, 7])
print(arr.shape)

reshaped_Arr = np.reshape(arr, (3, 1))
print(reshaped_Arr, reshaped_Arr.shape)

arr2 = np.array([
    [3, 4, 5],
    [6, 3, 2],
    [3, 4, 5],
    [6, 3, 2]
])

print(np.reshape(arr2, (6, 2)))