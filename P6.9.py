import matplotlib.pyplot as plt
import numpy as np

print("S115 BIJAL TRIPATHI")

fig, ax = plt.subplots(2,2, figsize=(10,8))

# Line Plot
ax[0,0].plot([1,2,3,4],[2,4,6,8], marker="o")
ax[0,0].set_title("Line Plot")

# Bar Chart
ax[0,1].bar(["A","B","C","D"], [10,20,15,25], color="orange")
ax[0,1].set_title("Bar Chart")

# Scatter Plot
x = [5,7,8,7,6,9,5]
y = [99,86,87,88,100,86,103]

ax[1,0].scatter(x, y, color="green", s=100)
ax[1,0].set_title("Scatter Plot")

# Histogram
data = np.random.randn(100)

ax[1,1].hist(data, bins=20, color="pink", edgecolor="black")
ax[1,1].set_title("Histogram")

plt.tight_layout()

plt.show()
