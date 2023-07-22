import numpy as np
import matplotlib.pyplot as plt

# y = f(x), y = sin(x)
x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.plot(x, y_tan)
# plt.xlabel("x-axis values")
# plt.ylabel("y-axis values")
# plt.title("Sin & Cosine & Tan Curve")
# plt.legend(['Sine', 'Cosine', 'Tan'])
# plt.show()

plt.subplot(3, 1, 1)
plt.plot(x, y_sin)
plt.title("Sin wave")

plt.subplot(3, 1, 2)
plt.plot(x, y_cos)
plt.title("Cos wave")

plt.subplot(3, 1, 3)
plt.plot(x, y_tan)
plt.title("Tan wave")
plt.show()

