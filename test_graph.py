import matplotlib.pyplot as plt
import random

WINDOW_SIZE = 50

x,y = [], []

plt.ion()
fig, ax = plt.subplots()
for i in range(1000):
    x.append(i)
    y.append(random.randint(0,10))

    ax.clear()
    ax.plot(x,y)
    left = max(0, i - WINDOW_SIZE)
    ax.set_xlim(left, left + WINDOW_SIZE)

    ax.set_ylim(0,10)

    plt.pause(0.2)


plt.ioff()
plt.show()