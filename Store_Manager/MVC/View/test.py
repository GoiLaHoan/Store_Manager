import numpy as np
import matplotlib.pyplot as plt

x = np.arange(11)+1
# x = [i for i in range(1, 11)]
y1 = [0.95, 0.95, 0.89, 0.8, 0.74, 0.65, 0.59, 0.51, 0.5, 0.48,0.5]
y2 = [0.90, 0.90, 0.90, 0.85, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90,0.6]


plt.bar(x, height=y1, width=0.1)
plt.bar(x+0.1, height=y2, width=0.1)
xlocs, xlabs = plt.xticks()
xlocs = [i + 1 for i in range(0, 10)]
xlabs = [i / 2 for i in range(0, 10)]
plt.xlabel('Max Sigma')
plt.ylabel('Test Accuracy')
plt.xticks(xlocs, xlabs)
plt.show()
