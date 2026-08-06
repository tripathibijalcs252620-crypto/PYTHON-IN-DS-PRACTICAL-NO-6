import matplotlib.pyplot as plt
import numpy as np

print("S115 BIJAL TRIPATHI")

data = np.random.randn(100)

plt.hist(data, bins=20, color="purple", edgecolor="black")

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()
