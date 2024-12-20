###
# A program that draws the function y = sin(x)
#
import math
import matplotlib.pyplot as plt
x = []
y = []

for i in range(361):
    x = x + [i]

for n in range(361):
    y = y + [math.sin(math.radians(n))]

plt.plot(x, y)
plt.grid(True)
plt.show()
