import random
import matplotlib.pyplot as plt
def f1(x, y):
    return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
def f2(x, y):
    return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
def f3(x, y):
    return 0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6
def f4(x, y):
    return 0,  0.16*y

x = [0]
y = [0]
for i in range(100000):
    result = random.choices([f1(x[i], y[i]), f2(x[i], y[i]), f3(x[i], y[i]), f4(x[i], y[i])], [0.85, 0.07, 0.07, 0.01])[0]
    x.append(result[0])
    y.append(result[1])

plt.figure(figsize=(5, 8))
plt.axis('off')
plt.title("Barnsley fern")
plt.scatter(x, y, s=0.03, c='green')
plt.show()