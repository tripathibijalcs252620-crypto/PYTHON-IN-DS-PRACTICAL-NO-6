import matplotlib.pyplot as plt

print("S115 BIJAL TRIPATHI")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

plt.plot(months,
         sales_2023,
         color="blue",
         linestyle="--",
         marker="o",
         linewidth=2,
         label="Sales 2023")

plt.plot(months,
         sales_2024,
         color="green",
         linestyle="-",
         marker="s",
         linewidth=2,
         label="Sales 2024")

plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()

highest = max(sales_2024)
index = sales_2024.index(highest)

plt.annotate(
    "Highest Sales",
    xy=(months[index], highest),
    xytext=(months[index], highest + 30),
    arrowprops=dict(facecolor="black", shrink=0.05)
)

plt.grid(True)

plt.savefig("sales_comparison.png")

plt.show()
