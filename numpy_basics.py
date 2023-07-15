import numpy as np

slist = [[1, 2, 4], [5, 6, 7]]
print(slist[0][0])

arr = np.array([[1, 4, 6],  [4, 7, 9]])
print(arr, arr.shape, type(arr), arr.size)

# arr = np.arange(1, 100, 5)
# print(arr)

# arr = np.linspace(5, 15, 20)
# print(arr)

print(arr[0,0])
print(arr[:,1])
# print(arr[0,2])
# print(arr[1,0])
# print(arr[1,1])
# print(arr[1,2])

print(arr[0, 1:])