import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   y = y + [n**2 - 3]


# print chart
plt.plot(x, y)
plt.grid(True)
plt.show()
