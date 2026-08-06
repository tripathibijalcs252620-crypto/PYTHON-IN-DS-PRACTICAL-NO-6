import matplotlib.pyplot as plt

print("S115 BIJAL TRIPATHI")

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot([1,2,3,4],[2,4,6,8], marker="o")
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.bar(["A","B","C","D"], [10,20,15,25], color="green")
plt.title("Bar Chart")

plt.tight_layout()

plt.show()
